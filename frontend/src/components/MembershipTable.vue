<template>
    <table class="table table-striped">
        <thead>
            <tr>
                <th scope="col">#</th>
                <th scope="col">Team</th>
                <th scope="col">League</th>
                <th scope="col">Status</th>
                <th scope="col">Date Joined</th>
                <th scope="col">Actions</th>
            </tr>
        </thead>
        <tbody>
            <tr v-for="(membership, index) in memberships" :key="membership.id">
                <th scope="row">{{ index + 1 }}</th>
                <td>{{ membership.team.name }}</td>
                <td>{{ membership.league.name }}</td>
                <td>
                    <span :class="{'text-success': membership.still_active, 'text-danger': !membership.still_active}">
                        {{ membership.still_active ? 'Active' : 'Inactive' }}
                    </span>
                </td>
                <td>{{ new Date(membership.date_joined).toLocaleDateString() }}</td>
                <td>
                    <button 
                        class="btn btn-sm btn-primary me-2"
                        @click="$emit('edit-membership', membership)"
                    > Edit
                    </button>
                    <button 
                        class="btn btn-sm btn-danger me-2"
                        @click="$emit('delete-membership', membership)"
                    > Delete
                    </button>
                </td>
            </tr>
        </tbody>
    </table>
</template>

<script>
export default {
    props: {
        memberships: Array
    },
    emits: ['edit-membership', 'delete-membership']
}
</script>

<style scoped>
td, th {
    vertical-align: middle;
}
</style>