<template>
    <table class="table">
        <thead>
            <tr>
                <th scope="col">#</th>
                <th scope="col">Team</th>
                <th scope="col">City</th>
                <th scope="col">Captain</th>
                <th scope="col">Coach</th>
                <th scope="col">Year Founded</th>
                <th scope="col">Actions</th>
            </tr>
        </thead>
        <tbody>
            <tr v-for="(team, index) in teams" :key="team.id">
                <th scope="row">{{ index + 1 }}</th>
                <td>{{ team.name }}</td>
                <td>{{ team.city }}</td>
                <td>{{ team.captain }}</td>
                <td>{{ team.coach }}</td>
                <td>{{ team.year_founded }}</td>
                <td>
                    <button 
                        class="btn btn-sm btn-primary me-2"
                        @click="editTeam(team)"
                    >
                        <i class="bi bi-pencil-square"></i>
                    </button>
                    <button 
                        class="btn btn-sm btn-danger"
                        @click="$emit('delete-team', team)"
                    >
                        <i class="bi bi-trash"></i>
                    </button>
                </td>
            </tr>
        </tbody>
    </table>
</template>

<script>
export default {
    props: {
        teams: Array
    },
    methods: {
        editTeam(team) {
            this.$emit('edit-team', team);
        }
    }
}
</script>

<style scoped>
td, th {
    vertical-align: middle;
}
</style>