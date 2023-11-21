from django.urls import get_resolver, URLPattern, URLResolver

# Lista de namespaces que NÃO devem ser expostos
NOT_PERMITTED_NAMESPACES = ['admin']

def get_full_pattern(url_patterns, prefix="", current_namespace=None):
    routes = []

    for url_pattern in url_patterns:
        # Se for um URLResolver, verificar o namespace
        if isinstance(url_pattern, URLResolver):
            next_namespace = url_pattern.namespace if url_pattern.namespace else current_namespace
            # Se o namespace atual não estiver na lista de não permitidos, continuar a processar
            if next_namespace not in NOT_PERMITTED_NAMESPACES:
                nested_routes = get_full_pattern(url_pattern.url_patterns, prefix + str(url_pattern.pattern), next_namespace)
                routes.extend(nested_routes)
        elif isinstance(url_pattern, URLPattern):
            if url_pattern.name and (current_namespace is None or current_namespace not in NOT_PERMITTED_NAMESPACES):
                full_pattern = prefix + str(url_pattern.pattern)
                routes.append({'name': url_pattern.name, 'pattern': full_pattern})

    return routes

def get_routes():
    return get_full_pattern(get_resolver().url_patterns)
