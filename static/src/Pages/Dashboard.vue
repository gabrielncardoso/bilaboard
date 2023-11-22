<script>
import AppLayout from '../Layouts/AppLayout.vue'

export default {
    components: {
        AppLayout
    },
    data() {
        return {
            user_groups: this.$page.props.user_groups
        }
    },
}

</script>
  
<template>
    <AppLayout>
        <div class="grid grid-cols-1 gap-4 sm:grid-cols-2">
            <div v-for="group in user_groups" :key="group.email"
                class="relative flex items-center space-x-3 rounded-lg border border-gray-300 bg-white px-6 py-5 shadow-sm focus-within:ring-2 focus-within:ring-indigo-500 focus-within:ring-offset-2 hover:border-gray-400">
                <div class="flex-shrink-0">
                    <!-- TODO -->
                    <img class="h-10 w-10 rounded-full" src="#" alt="" />
                </div>
                <div class="min-w-0 flex-1">
                    <a :href="$buildUrl('groupdetail', {name:'group_id', value: group.id})" class="focus:outline-none">
                        <span class="absolute inset-0" aria-hidden="true" />
                        <p class="text-sm font-medium text-gray-900">{{ group.name }}</p>
                    </a>
                </div>
            </div>
        </div>
    </AppLayout>
</template>