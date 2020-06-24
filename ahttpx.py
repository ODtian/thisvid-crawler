from httpx import AsyncClient


async def request(
    method: str,
    url,
    *,
    params=None,
    data=None,
    files=None,
    json=None,
    headers=None,
    cookies=None,
    auth=None,
    timeout=None,
    allow_redirects=True,
    verify=True,
    cert=None,
    trust_env=True,
    proxies=None,
    stream=False
):
    async with AsyncClient(
        cert=cert, verify=verify, timeout=timeout, trust_env=trust_env, proxies=proxies
    ) as client:
        return await getattr(client, "stream" if stream else "request")(
            method=method,
            url=url,
            data=data,
            files=files,
            json=json,
            params=params,
            headers=headers,
            cookies=cookies,
            auth=auth,
            allow_redirects=allow_redirects,
        )


async def get(
    url,
    *,
    params=None,
    headers=None,
    cookies=None,
    auth=None,
    allow_redirects=True,
    cert=None,
    verify=True,
    timeout=None,
    trust_env=True,
    proxies=None,
    stream=False
):
    return await request(
        "GET",
        url,
        params=params,
        headers=headers,
        cookies=cookies,
        auth=auth,
        allow_redirects=allow_redirects,
        cert=cert,
        verify=verify,
        timeout=timeout,
        trust_env=trust_env,
        proxies=proxies,
    )


async def options(
    url,
    *,
    params=None,
    headers=None,
    cookies=None,
    auth=None,
    allow_redirects=True,
    cert=None,
    verify=True,
    timeout=None,
    trust_env=True,
    proxies=None,
    stream=False
):
    return await request(
        "OPTIONS",
        url,
        params=params,
        headers=headers,
        cookies=cookies,
        auth=auth,
        allow_redirects=allow_redirects,
        cert=cert,
        verify=verify,
        timeout=timeout,
        trust_env=trust_env,
        proxies=proxies,
    )


async def head(
    url,
    *,
    params=None,
    headers=None,
    cookies=None,
    auth=None,
    allow_redirects=False,
    cert=None,
    verify=True,
    timeout=None,
    trust_env=True,
    proxies=None,
    stream=False
):
    return await request(
        "HEAD",
        url,
        params=params,
        headers=headers,
        cookies=cookies,
        auth=auth,
        allow_redirects=allow_redirects,
        cert=cert,
        verify=verify,
        timeout=timeout,
        trust_env=trust_env,
        proxies=proxies,
    )


async def post(
    url,
    *,
    data=None,
    files=None,
    json=None,
    params=None,
    headers=None,
    cookies=None,
    auth=None,
    allow_redirects=True,
    cert=None,
    verify=True,
    timeout=None,
    trust_env=True,
    proxies=None,
    stream=False
):
    return await request(
        "POST",
        url,
        data=data,
        files=files,
        json=json,
        params=params,
        headers=headers,
        cookies=cookies,
        auth=auth,
        allow_redirects=allow_redirects,
        cert=cert,
        verify=verify,
        timeout=timeout,
        trust_env=trust_env,
        proxies=proxies,
    )


async def put(
    url,
    *,
    data=None,
    files=None,
    json=None,
    params=None,
    headers=None,
    cookies=None,
    auth=None,
    allow_redirects=True,
    cert=None,
    verify=True,
    timeout=None,
    trust_env=True,
    proxies=None,
    stream=False
):
    return await request(
        "PUT",
        url,
        data=data,
        files=files,
        json=json,
        params=params,
        headers=headers,
        cookies=cookies,
        auth=auth,
        allow_redirects=allow_redirects,
        cert=cert,
        verify=verify,
        timeout=timeout,
        trust_env=trust_env,
        proxies=proxies,
    )


async def patch(
    url,
    *,
    data=None,
    files=None,
    json=None,
    params=None,
    headers=None,
    cookies=None,
    auth=None,
    allow_redirects=True,
    cert=None,
    verify=True,
    timeout=None,
    trust_env=True,
    proxies=None,
    stream=False
):
    return await request(
        "PATCH",
        url,
        data=data,
        files=files,
        json=json,
        params=params,
        headers=headers,
        cookies=cookies,
        auth=auth,
        allow_redirects=allow_redirects,
        cert=cert,
        verify=verify,
        timeout=timeout,
        trust_env=trust_env,
        proxies=proxies,
    )


async def delete(
    url,
    *,
    params=None,
    headers=None,
    cookies=None,
    auth=None,
    allow_redirects=True,
    cert=None,
    verify=True,
    timeout=None,
    trust_env=True,
    proxies=None,
    stream=False
):
    return await request(
        "DELETE",
        url,
        params=params,
        headers=headers,
        cookies=cookies,
        auth=auth,
        allow_redirects=allow_redirects,
        cert=cert,
        verify=verify,
        timeout=timeout,
        trust_env=trust_env,
        proxies=proxies,
    )
