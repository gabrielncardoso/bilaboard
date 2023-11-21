from django.urls import get_resolver, URLPattern, URLResolver

# Lista de nomes de rotas permitidas
PERMITTED_ROUTES = []

# Lista de namespaces permitidos
PERMITTED_NAMESPACES = []

# Lista de caminhos permitidos (ex.: 'admin/')
PERMITTED_PATHS = ['bilaapp/']

def get_full_pattern(url_patterns, prefix="", current_namespace=""):
    routes = []

    for url_pattern in url_patterns:
        # Determinar o namespace atual, se houver
        new_namespace = current_namespace
        if isinstance(url_pattern, URLResolver):
            if url_pattern.namespace:
                new_namespace = url_pattern.namespace if not current_namespace else f"{current_namespace}:{url_pattern.namespace}"

        if isinstance(url_pattern, URLPattern):
            # Construir o caminho completo
            full_pattern = prefix + str(url_pattern.pattern)
            
            # Verificar se a rota está permitida pela lista de rotas, namespaces ou caminhos
            if (url_pattern.name and url_pattern.name in PERMITTED_ROUTES) or \
               (new_namespace in PERMITTED_NAMESPACES) or \
               any(full_pattern.startswith(path) for path in PERMITTED_PATHS):
                
                route_name = f"{new_namespace}:{url_pattern.name}" if new_namespace else url_pattern.name
                routes.append({'name': route_name, 'pattern': full_pattern})
        elif isinstance(url_pattern, URLResolver):
            # Chamar recursivamente para rotas aninhadas
            nested_routes = get_full_pattern(url_pattern.url_patterns, prefix + str(url_pattern.pattern), new_namespace)
            routes.extend(nested_routes)

    return routes

def get_routes():
    return get_full_pattern(get_resolver().url_patterns)
