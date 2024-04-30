import dnstwist


def get_data() -> list[dict]:
    data = dnstwist.run(domain='kaspi.kz', format='json')
    return data
