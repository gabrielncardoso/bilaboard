export default {
    install: (app, options) => {
        const routes = options.routes;
        const appUrl = options.appUrl;

        app.config.globalProperties.$getRoute = (routeName, params = {}) => {
            const route = routes.find(route => route.name === routeName);
            if (!route) {
                throw new Error(`Route not found: ${routeName}`);
            }

            let url = route.pattern;

            // Verificar se todos os parâmetros necessários estão presentes
            const missingParams = [];
            url = url.replace(/<\w+:(\w+)>/g, (match, paramName) => {
                if (params[paramName] === undefined) {
                    missingParams.push(paramName);
                    return match;
                }
                return params[paramName];
            });

            if (missingParams.length > 0) {
                throw new Error(`Missing parameters: ${missingParams.join(', ')}`);
            }

            return `${appUrl}/${url}`;
        }
    },
};
