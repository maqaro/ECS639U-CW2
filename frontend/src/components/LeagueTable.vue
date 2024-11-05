<template>
    <table class="table table-striped">
        <thead>
            <tr>
                <th>Name</th>
                <th>Location</th>
                <th>Actions</th>
            </tr>
        </thead>
        <tbody>
            <tr v-for="league in leagues" :key="league.id">
                <td>{{ league.name }}</td>
                <td>{{ league.location }}</td>
                <td>
                    <button class="btn btn-sm btn-primary me-2" @click="$emit('edit-league', league)">Edit</button>
                    <button class="btn btn-sm btn-danger me-2" @click="$emit('delete-league', league)">Delete</button>
                </td>
            </tr>
        </tbody>
    </table>
</template>

<script>
export default {
    props: {
        leagues: Array
    },
    emits: ['edit-league', 'delete-league']
};
</script>

<style scoped>
</style>