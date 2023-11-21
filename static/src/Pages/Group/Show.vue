<script>
import AppLayout from '../../Layouts/AppLayout.vue';

export default {
    components: {
        AppLayout
    },
}

</script>


<template>
    <AppLayout>
        <h1>Group detail</h1>

        <pre>
            {{ $page.props.group }}
        </pre>
    </AppLayout>
</template>