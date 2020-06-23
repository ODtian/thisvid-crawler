function a1(a, b, c, d) {
    for (var f in a)
        if (0 == a[f].indexOf(b)) {
            var g = a[f].substring(b.length).split(b[b.length - 1]);
            if (g[0] >= 0) {
                var h = g[6].substring(0, 2 * parseInt(d)),
                    i = a2(a, c, d);
                if (i && h) {
                    for (var j = h, k = h.length - 1; k >= 0; k--) {
                        for (var l = k, m = k; m < i.length; m++)
                            l += parseInt(i[m]);
                        for (; l >= h.length;)
                            l -= h.length;
                        for (var n = "", o = 0; o < h.length; o++)
                            n += o == k ? h[l] : o == l ? h[k] : h[o];
                        h = n
                    }
                    g[6] = g[6].replace(j, h),
                        g.splice(0, 1),
                        a[f] = g.join(b[b.length - 1])
                }
            }
        }
    return a.video_url
}

function a2(a, b, c) {
    var e, g, h, i, j, k, l, m, n, d = "",
        f = "",
        o = parseInt;
    for (e in a)
        if (e.indexOf(b) > 0 && a[e].length == o(c)) {
            d = a[e];
            break
        }
    if (d) {
        for (f = "",
            g = 1; g < d.length; g++)
            f += o(d[g]) ? o(d[g]) : 1;
        for (j = o(f.length / 2),
            k = o(f.substring(0, j + 1)),
            l = o(f.substring(j)),
            g = l - k,
            g < 0 && (g = -g),
            f = g,
            g = k - l,
            g < 0 && (g = -g),
            f += g,
            f *= 2,
            f = "" + f,
            i = o(c) / 2 + 2,
            m = "",
            g = 0; g < j + 1; g++)
            for (h = 1; h <= 4; h++)
                n = o(d[g + h]) + o(f[g]),
                n >= i && (n -= i),
                m += n;
        return m
    }
    return d
}