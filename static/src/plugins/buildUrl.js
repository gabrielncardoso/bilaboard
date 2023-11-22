export default {
    install: (app, options) => {
        // injeta um método "$buildUrl()" disponível globalmente
        app.config.globalProperties.$buildUrl = (routeName, param) => {

            const result = options.routes.find((route) => route.name == routeName);
            let routeFormatted = result.pattern.split('/');

            const isGroupId = (element) => element.includes(param.name);

            const index = routeFormatted.findIndex(isGroupId)

            routeFormatted[index] = param.value;

            let url = options.appUrl + routeFormatted.join('/')

            return url
        }
    }
}