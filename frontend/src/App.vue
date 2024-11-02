<template>
    <div class="container pt-3">
        <div class="h1 text-center border rounded bg-light p-2 mb-3">
            {{ title }}
        </div>

        <Tabs>
            <template v-slot:teams>
                <button class="btn btn-sm btn-success mb-3" data-bs-toggle="modal" data-bs-target="#addTeamModal">
                    <i class="bi bi-plus"></i> Add Team
                </button>

                <!-- Team Modal -->
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
                                <button type="button" class="btn btn-secondary" data-bs-dismiss="modal">Close</button>
                                <button type="button" class="btn btn-primary" @click="isEditing ? updateTeam() : createTeam()" data-bs-dismiss="modal">
                                    Save
                                </button>
                            </div>
                        </div>
                    </div>
                </div>

                <TeamTable :teams="teams" @delete-team="deleteTeam" @edit-team="editTeam" />
            </template>

            <template v-slot:leagues>
                <button class="btn btn-sm btn-success mb-3" data-bs-toggle="modal" data-bs-target="#addLeagueModal">
                    <i class="bi bi-plus"></i> Add League
                </button>

                <div class="modal fade" id="addLeagueModal" tabindex="-1" aria-labelledby="addLeagueModalLabel" aria-hidden="true">
                    <div class="modal-dialog">
                        <div class="modal-content">
                            <div class="modal-header">
                                <h1 class="modal-title fs-5" id="addLeagueModalLabel">{{ isEditingLeague ? 'Edit League' : 'Add League' }}</h1>
                                <button type="button" class="btn-close" data-bs-dismiss="modal" aria-label="Close"></button>
                            </div>
                            <div class="modal-body">
                                <div class="mb-3">
                                    <label for="leagueName" class="form-label">Name</label>
                                    <input v-model="newLeague.name" type="text" class="form-control" id="leagueName">
                                </div>
                                <div class="mb-3">
                                    <label for="location" class="form-label">Location</label>
                                    <input v-model="newLeague.location" type="text" class="form-control" id="location">
                                </div>
                            </div>
                            <div class="modal-footer">
                                <button type="button" class="btn btn-secondary" data-bs-dismiss="modal">Close</button>
                                <button type="button" class="btn btn-primary" @click="isEditingLeague ? updateLeague() : createLeague()" data-bs-dismiss="modal">
                                    Save
                                </button>
                            </div>
                        </div>
                    </div>
                </div>

                <LeagueTable :leagues="leagues" @delete-league="deleteLeague" @edit-league="editLeague" />
            </template>
        </Tabs>
    </div>
</template>

<script>
import Tabs from './components/Tabs.vue';
import TeamTable from './components/TeamTable.vue';
import LeagueTable from './components/LeagueTable.vue';

const baseUrl = 'http://localhost:8000';

export default {
    components: {
        Tabs,
        TeamTable,
        LeagueTable
    },
    data() {
        return {
            title: 'Team & League Information',
            teams: [],
            leagues: [],
            newTeam: {
                name: '',
                city: '',
                captain: '',
                coach: '',
                year_founded: 1900
            },
            newLeague: {
                name: '',
                location: ''
            },
            isEditing: false,
            isEditingLeague: false,
            editingTeamId: null,
            editingLeagueId: null
        };
    },
    async mounted() {
        // Fetch Teams Data
        const teamsResponse = await fetch(`${baseUrl}/api/teams/`);
        const teamsData = await teamsResponse.json();
        this.teams = teamsData.teams;

        // Fetch Leagues Data
        const leaguesResponse = await fetch(`${baseUrl}/api/leagues/`);
        const leaguesData = await leaguesResponse.json();
        this.leagues = leaguesData.leagues;
    },
    methods: {
        async deleteTeam(team) {
            if (confirm(`Are you sure you want to delete team '${team.name}'?`)) {
                const response = await fetch(`${baseUrl}/api/teams/${team.id}/`, {
                    method: 'DELETE',
                });
                if (response.ok) {
                    this.teams = this.teams.filter(t => t.id !== team.id);
                }
            }
        },
        async createTeam() {
            const response = await fetch(`${baseUrl}/api/teams/`, {
                method: 'POST',
                headers: {
                    'Content-Type': 'application/json'
                },
                body: JSON.stringify(this.newTeam)
            });
            const newTeam = await response.json();
            this.teams.push(newTeam);
            this.resetForm();
        },
        async updateTeam() {
            const response = await fetch(`${baseUrl}/api/teams/${this.editingTeamId}/`, {
                method: 'PUT',
                headers: {
                    'Content-Type': 'application/json'
                },
                body: JSON.stringify(this.newTeam)
            });
            const updatedTeam = await response.json();
            const index = this.teams.findIndex(t => t.id === this.editingTeamId);
            this.teams.splice(index, 1, updatedTeam);
            this.resetForm();
        },
        editTeam(team) {
            this.isEditing = true;
            this.editingTeamId = team.id;
            this.newTeam = { ...team };
            const modal = new bootstrap.Modal(document.getElementById('addTeamModal'));
            modal.show();
        },
        resetForm() {
            this.newTeam = {
                name: '',
                city: '',
                captain: '',
                coach: '',
                year_founded: 1900
            };
            this.isEditing = false;
            this.editingTeamId = null;
        },
        async deleteLeague(league) {
            if (confirm(`Are you sure you want to delete league '${league.name}'?`)) {
                const response = await fetch(`${baseUrl}/api/leagues/${league.id}/`, {
                    method: 'DELETE',
                });
                if (response.ok) {
                    this.leagues = this.leagues.filter(l => l.id !== league.id);
                }
            }
        },
        async createLeague() {
            const response = await fetch(`${baseUrl}/api/leagues/`, {
                method: 'POST',
                headers: {
                    'Content-Type': 'application/json'
                },
                body: JSON.stringify(this.newLeague)
            });
            const newLeague = await response.json();
            this.leagues.push(newLeague);
            this.resetLeagueForm();
        },
        async updateLeague() {
            const response = await fetch(`${baseUrl}/api/leagues/${this.editingLeagueId}/`, {
                method: 'PUT',
                headers: {
                    'Content-Type': 'application/json'
                },
                body: JSON.stringify(this.newLeague)
            });
            const updatedLeague = await response.json();
            const index = this.leagues.findIndex(l => l.id === this.editingLeagueId);
            this.leagues.splice(index, 1, updatedLeague);
            this.resetLeagueForm();
        },
        editLeague(league) {
            this.isEditingLeague = true;
            this.editingLeagueId = league.id;
            this.newLeague = { ...league };
            const modal = new bootstrap.Modal(document.getElementById('addLeagueModal'));
            modal.show();
        },
        resetLeagueForm() {
            this.newLeague = {
                name: '',
                location: ''
            };
            this.isEditingLeague = false;
            this.editingLeagueId = null;
        }
    }
};
</script>

<style scoped>
</style>

<style scoped>
</style>
