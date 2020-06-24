import asyncio
import re
import time
from queue import Empty, Queue
from threading import Thread

import execjs
import lxml.html
import ahttpx


try:
    import uvloop
except ImportError:
    print(
        "[WARNING] Module uvloop is not installed, use default loop instead. Using uvloop can bring significant performance improvement, install it by 'pip install uvloop'.",
    )
else:
    asyncio.set_event_loop_policy(uvloop.EventLoopPolicy())


async def crawl_page(url):
    print("[INFO] Fetching page: {}".format(url))
    try:
        r = await ahttpx.get(url, headers=headers)
        html = r.text
        tree = lxml.html.fromstring(html)
    except Exception as e:
        import traceback

        print(
            "[ERROR] Error occurred when fetching page {}\n"
            "--- Traceback Start ---\n"
            "{}"
            "--- Traceback End ---".format(url, traceback.format_exc())
        )
        raise e
    else:
        return [
            (a.attrib.get("href"), a.attrib.get("title"))
            for a in tree.xpath("//a[@class='tumbpu']")
        ]


async def get_video_url(task):
    video_url, name = task
    name += ".mp4"
    # name = name.replace(" ", "_")

    print("[INFO] Fetching video: {}".format(video_url))
    try:
        r = await ahttpx.get(video_url, headers=headers)
        r.raise_for_status()
        html = r.text
        if "video is a private" in html:
            print("[ERROR] This video is private: {}".format(video_url))
            return
        # tree = lxml.html.fromstring(html)
        # name = tree.xpath("//h1")[0].text_content() + ".mp4"

        # cf_email = tree.xpath("//a[@class='__cf_email__']")
        # if len(cf_email) > 0:
        #     name_prefix_encode = cf_email[0].attrib.get("data-cfemail")
        #     name_prefix = cf_decode_email(name_prefix_encode)
        #     name_replace = cf_email[0].text
        #     name = name.replace(name_replace, name_prefix)

        pattern_url = re.compile(r"video_url: '(.*?)'", re.I | re.M).findall(html)[0]
        # pattern_code = re.compile(r"license_code: '(.*?)'", re.I | re.M).findall(html)[
        #     0
        # ]
        video_url = get_real_url(video_url=pattern_url, license_code="$478310915780312")
    except IndexError as e:
        print("[ERROR] No video found: {}".format(video_url))
        raise e
    except Exception as e:
        import traceback

        print(
            "[ERROR] Error occurred when fetching page {}\n"
            "--- Traceback Start ---\n"
            "{}"
            "--- Traceback End ---".format(video_url, traceback.format_exc())
        )
        raise e
    else:
        return (video_url, name)


def get_real_url(**data):
    return js_ctx.call("a1", data, "function/", "code", "16px")


# def cf_decode_email(encodedString):
#     r = int(encodedString[:2], 16)
#     email = "".join(
#         [
#             chr(int(encodedString[i : i + 2], 16) ^ r)
#             for i in range(2, len(encodedString), 2)
#         ]
#     )
#     return email


def put_task(task):
    now["now_task"] += 1
    q.put(task)


def get_task():
    try:
        task = q.get(timeout=0.01)
    except Empty:
        return
    else:
        return task


def task_done():
    now["now_task"] -= 1


def finished():
    return now["now_task"] == 0 and now["finished"]


async def excutor(task):
    try:
        if not task[2] <= 0:
            result = await get_video_url(task[:2])
            print(result)
            videos.append(result)
    except Exception:
        task[2] -= 1
        put_task(task)
    finally:
        task_done()


async def task_pusher():
    for page in pages:
        url = page_url.format(page=page)
        try:
            result = await crawl_page(url)
        except Exception:
            pages.append(page)
        else:
            [put_task(r) for r in result]
    now["finished"] = True


def start_loop(loop):
    def loop_runner():
        loop.run_forever()

    loop_thread = Thread(target=loop_runner, daemon=True)
    loop_thread.start()
    return loop_thread


def run_loop(loop):
    while True:
        if finished():
            break
        else:
            task = get_task()

            if not task:
                continue
            else:
                task = task[:2] + (task[2:] or (retry,))
            add_to_loop(excutor(task), loop)

        time.sleep(0.01)


def add_to_loop(excutor, loop):
    asyncio.run_coroutine_threadsafe(excutor, loop)


with open("./fuck.js", "r") as f:
    js_ctx = execjs.compile(f.read())

headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) "
    "AppleWebKit/537.36 (KHTML, like Gecko) "
    "Chrome/84.0.4147.30 Safari/537.36 Edg/84.0.522.11"
}
page_url = "https://thisvid.com/latest-updates/{page}/"
retry = 3
pages = [i for i in range(1, 5200)]


now = {"now_task": 0, "finished": False}
q = Queue()
videos = []

loop = asyncio.get_event_loop()

try:
    start_loop(loop)
    add_to_loop(task_pusher(), loop)
    run_loop(loop)
except KeyboardInterrupt:
    print("Stopped, will save finished.")
except Exception as e:
    print("\nOops! Error occurred, will save finished.")
    print(e)
finally:
    loop.call_soon_threadsafe(loop.stop)
    with open("./downloads.txt", "w") as f:
        for item in set(videos):
            if item:
                url, name = item
                f.write("{}\n    out={}\n".format(url, name))


# def iter_lines(f):
#     while True:
#         line = f.readline()
#         if line:
#             yield line
#         else:
#             break


# with open("./downloads_nhentai_sorted.txt", "w") as f:
#     with open("./downloads_nhentai.txt", "r") as f2:
#         f.writelines(
#             sorted(iter_lines(f2), key=lambda line: int(line[:-2]), reverse=True)
#         )
