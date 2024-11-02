<template>
    <div class="container pt-3">
        <div class="h1 text-center border rounded bg-light p-2 mb-3">
            {{ title }}
        </div>

        <button class="btn btn-sm btn-success mb-3" data-bs-toggle="modal" data-bs-target="#addTeamModal">
            <i class="bi bi-plus"></i> Add Team 
        </button>

        <!-- Modal -->
        <div class="modal fade" id="addTeamModal" tabindex="-1" aria-labelledby="addTeamModalLabel" aria-hidden="true">
            <div class="modal-dialog">
                <div class="modal-content">
                    <div class="modal-header">
                        <h1 class="modal-title fs-5" id="addTeamModalLabel">{{ isEditing ? 'Edit Team' : 'Add Team' }}</h1>
                        <button type="button" class="btn-close" data-bs-dismiss="modal" aria-label="Close"></button>
                    </div>
                    <div class="modal-body">
                        <div class="mb-3">
                            <label for="name" class="form-label">Name</label>
                            <input v-model="newTeam.name" type="text" class="form-control" id="name">
                        </div>
                        <div class="mb-3">
                            <label for="city" class="form-label">City</label>
                            <input v-model="newTeam.city" type="text" class="form-control" id="city">
                        </div>
                        <div class="mb-3">
                            <label for="captain" class="form-label">Captain</label>
                            <input v-model="newTeam.captain" type="text" class="form-control" id="captain">
                        </div>
                        <div class="mb-3">
                            <label for="coach" class="form-label">Coach</label>
                            <input v-model="newTeam.coach" type="text" class="form-control" id="coach">
                        </div>
                        <div class="mb-3">
                            <label for="year_founded" class="form-label">Year Founded</label>
                            <input v-model="newTeam.year_founded" type="number" class="form-control" id="year_founded">
                        </div>
                    </div>
                    <div class="modal-footer">
                        <button type="button" class="btn btn-secondary" data-bs-dismiss="modal">
                            Close
                        </button>
                        <button type="button" class="btn btn-primary" @click="isEditing ? updateTeam() : createTeam()" data-bs-dismiss="modal">
                            Save
                        </button>
                    </div>
                </div>
            </div>
        </div>

        <TeamTable 
            :teams="teams"
            @delete-team="deleteTeam"
            @edit-team="editTeam"
        />
    </div>
</template>
  
<script>
import TeamTable from './components/TeamTable.vue'

const baseUrl = 'http://localhost:8000'

export default {
    components: {
        TeamTable
    },
    data() {
        return {
            title: 'Team Information',
            teams: [],
            newTeam: {
                name: '',
                city: '',
                captain: '',
                coach: '',
                year_founded: 1900
            },
            isEditing: false,
            editingTeamId: null
        }
    },
    async mounted() {
        const response = await fetch(`${baseUrl}/api/teams/`)
        const data = await response.json()
        this.teams = data.teams;
    },
    methods: {
        async deleteTeam(team) {
            if (confirm(`Are you sure you want to delete team '${team.name}'?`)) {
                const response = await fetch(`${baseUrl}/api/teams/${team.id}/`, {
                    method: 'DELETE',
                })
                if (response.ok)
                    this.teams = this.teams.filter(t => t.id !== team.id)
            }
        },
        async createTeam() {
            const response = await fetch(`${baseUrl}/api/teams/`, {
                method: 'POST',
                headers: {
                    'Content-Type': 'application/json'
                },
                body: JSON.stringify(this.newTeam)
            })
            const newTeam = await response.json()
            this.teams.push(newTeam)
            this.resetForm()
        },
        async updateTeam() {
            const response = await fetch(`${baseUrl}/api/teams/${this.editingTeamId}/`, {
                method: 'PUT',
                headers: {
                    'Content-Type': 'application/json'
                },
                body: JSON.stringify(this.newTeam)
            })
            const updatedTeam = await response.json()
            const index = this.teams.findIndex(t => t.id === this.editingTeamId)
            this.teams.splice(index, 1, updatedTeam)
            this.resetForm()
        },
        editTeam(team) {
            this.isEditing = true
            this.editingTeamId = team.id
            this.newTeam = { ...team }
            const modal = new bootstrap.Modal(document.getElementById('addTeamModal'))
            modal.show()
        },
        resetForm() {
            this.newTeam = {
                name: '',
                city: '',
                captain: '',
                coach: '',
                year_founded: 1900
            }
            this.isEditing = false
            this.editingTeamId = null
        }
    }
}
</script>

<style scoped>
</style>