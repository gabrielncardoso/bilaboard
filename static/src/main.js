import { createApp, h } from 'vue'
import { createInertiaApp } from '@inertiajs/vue3'
import getRoutesPlugin from './plugins/getRoutes'
import buildUrl from './plugins/buildUrl'
import "./assets/css/main.css"

createInertiaApp({
  resolve: name => {
    const pages = import.meta.glob('./Pages/**/*.vue', { eager: true })
    return pages[`./Pages/${name}.vue`]
  },
  setup({ el, App, props, plugin }) {
    createApp({ render: () => h(App, props) })
      .use(plugin)
      .use(buildUrl, {routes: props.initialPage.props.routes, appUrl: props.initialPage.props.app_url})
      .use(getRoutesPlugin, {routes: props.initialPage.props.routes, appUrl: props.initialPage.props.app_url})
      .mount(el)
  },
})