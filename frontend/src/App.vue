<template>
    <div class="container pt-3">
        <div class="h1 text-center border rounded bg-light p-2 mb-3">
            {{ title }}
        </div>

        <Tabs>
            <template #teams>
                <button class="btn btn-sm btn-success mb-3" data-bs-toggle="modal" data-bs-target="#addTeamModal">
                    <i class="bi bi-plus"></i> Add Team 
                </button>
                <TeamTable 
                    :teams="teams"
                    @delete-team="deleteTeam"
                    @edit-team="editTeam"
                />
            </template>

            <template #leagues>
                <button class="btn btn-sm btn-success mb-3" data-bs-toggle="modal" data-bs-target="#addLeagueModal">
                    <i class="bi bi-plus"></i> Add League
                </button>
                <LeagueTable 
                    :leagues="leagues"
                    @edit-league="editLeague"
                    @delete-league="deleteLeague"
                />
            </template>

            <template #memberships>
                <button class="btn btn-sm btn-success mb-3" data-bs-toggle="modal" data-bs-target="#addMembershipModal">
                    <i class="bi bi-plus"></i> Add Membership
                </button>
                <MembershipTable 
                    :memberships="memberships"
                    @edit-membership="editMembership"
                    @delete-membership="deleteMembership"
                />
            </template>
        </Tabs>

        <!-- Team Modal -->
        <div class="modal fade" id="addTeamModal" tabindex="-1" aria-labelledby="addTeamModalLabel" aria-hidden="true">
            <div class="modal-dialog">
                <div class="modal-content">
                    <div class="modal-header">
                        <h1 class="modal-title fs-5" id="addTeamModalLabel">Add Team</h1>
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
                        <button type="button" class="btn btn-primary" @click="createTeam()" data-bs-dismiss="modal">
                            Save
                        </button>
                    </div>
                </div>
            </div>
        </div>

        <!-- League Modal -->
        <!-- Add League Modal -->
        <div class="modal fade" id="addLeagueModal" tabindex="-1" aria-labelledby="addLeagueModalLabel" aria-hidden="true">
            <div class="modal-dialog">
                <div class="modal-content">
                    <div class="modal-header">
                        <h1 class="modal-title fs-5" id="addLeagueModalLabel">Add League</h1>
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
                        <button type="button" class="btn btn-primary" @click="createLeague()" data-bs-dismiss="modal">
                            Save
                        </button>
                    </div>
                </div>
            </div>
        </div>

        <!-- Edit Team Modal -->
        <div class="modal fade" id="editTeamModal" tabindex="-1" aria-labelledby="editTeamModalLabel" aria-hidden="true">
            <div class="modal-dialog">
                <div class="modal-content">
                    <div class="modal-header">
                        <h1 class="modal-title fs-5" id="editTeamModalLabel">Edit Team</h1>
                        <button type="button" class="btn-close" data-bs-dismiss="modal" aria-label="Close"></button>
                    </div>
                    <div class="modal-body">
                        <div class="mb-3">
                            <label for="editName" class="form-label">Name</label>
                            <input v-model="editingTeam.name" type="text" class="form-control" id="editName">
                        </div>
                        <div class="mb-3">
                            <label for="editCity" class="form-label">City</label>
                            <input v-model="editingTeam.city" type="text" class="form-control" id="editCity">
                        </div>
                        <div class="mb-3">
                            <label for="editCaptain" class="form-label">Captain</label>
                            <input v-model="editingTeam.captain" type="text" class="form-control" id="editCaptain">
                        </div>
                        <div class="mb-3">
                            <label for="editCoach" class="form-label">Coach</label>
                            <input v-model="editingTeam.coach" type="text" class="form-control" id="editCoach">
                        </div>
                        <div class="mb-3">
                            <label for="editYearFounded" class="form-label">Year Founded</label>
                            <input v-model="editingTeam.year_founded" type="number" class="form-control" id="editYearFounded">
                        </div>
                    </div>
                    <div class="modal-footer">
                        <button type="button" class="btn btn-secondary" data-bs-dismiss="modal">Close</button>
                        <button type="button" class="btn btn-primary" @click="updateTeam()" data-bs-dismiss="modal">
                            Save Changes
                        </button>
                    </div>
                </div>
            </div>
        </div>

        <!-- Edit League Modal -->
        <div class="modal fade" id="editLeagueModal" tabindex="-1" aria-labelledby="editLeagueModalLabel" aria-hidden="true">
            <div class="modal-dialog">
                <div class="modal-content">
                    <div class="modal-header">
                        <h1 class="modal-title fs-5" id="editLeagueModalLabel">Edit League</h1>
                        <button type="button" class="btn-close" data-bs-dismiss="modal" aria-label="Close"></button>
                    </div>
                    <div class="modal-body">
                        <div class="mb-3">
                            <label for="editLeagueName" class="form-label">Name</label>
                            <input v-model="editingLeague.name" type="text" class="form-control" id="editLeagueName">
                        </div>
                        <div class="mb-3">
                            <label for="editLocation" class="form-label">Location</label>
                            <input v-model="editingLeague.location" type="text" class="form-control" id="editLocation">
                        </div>
                    </div>
                    <div class="modal-footer">
                        <button type="button" class="btn btn-secondary" data-bs-dismiss="modal">Close</button>
                        <button type="button" class="btn btn-primary" @click="updateLeague()" data-bs-dismiss="modal">
                            Save Changes
                        </button>
                    </div>
                </div>
            </div>
        </div>

        <!-- Membership Modal -->
        <div class="modal fade" id="addMembershipModal" tabindex="-1" aria-labelledby="addMembershipModalLabel" aria-hidden="true">
            <div class="modal-dialog">
                <div class="modal-content">
                    <div class="modal-header">
                        <h1 class="modal-title fs-5" id="addMembershipModalLabel">Add Membership</h1>
                        <button type="button" class="btn-close" data-bs-dismiss="modal" aria-label="Close"></button>
                    </div>
                    <div class="modal-body">
                        <div class="mb-3">
                            <label for="membershipTeam" class="form-label">Team</label>
                            <select 
                                v-model="newMembership.team_id" 
                                class="form-select" 
                                id="membershipTeam"
                            >
                                <option v-for="team in teams" :key="team.id" :value="team.id">
                                    {{ team.name }}
                                </option>
                            </select>
                        </div>
                        <div class="mb-3">
                            <label for="membershipLeague" class="form-label">League</label>
                            <select 
                                v-model="newMembership.league_id" 
                                class="form-select" 
                                id="membershipLeague"
                            >
                                <option v-for="league in leagues" :key="league.id" :value="league.id">
                                    {{ league.name }}
                                </option>
                            </select>
                        </div>
                        <div class="mb-3">
                            <label for="membershipDate" class="form-label">Date Joined</label>
                            <input 
                                type="date" 
                                class="form-control" 
                                id="membershipDate"
                                v-model="newMembership.date_joined"
                            >
                        </div>
                        <div class="mb-3 form-check">
                            <input 
                                type="checkbox" 
                                class="form-check-input" 
                                id="membershipActive"
                                v-model="newMembership.still_active"
                            >
                            <label class="form-check-label" for="membershipActive">Still Active</label>
                        </div>
                    </div>
                    <div class="modal-footer">
                        <button type="button" class="btn btn-secondary" data-bs-dismiss="modal">Close</button>
                        <button type="button" class="btn btn-primary" @click="createMembership()" data-bs-dismiss="modal">
                            Save
                        </button>
                    </div>
                </div>
            </div>
        </div>

        <!-- Edit Membership Modal -->
        <div class="modal fade" id="editMembershipModal" tabindex="-1" aria-labelledby="editMembershipModalLabel" aria-hidden="true">
            <div class="modal-dialog">
                <div class="modal-content">
                    <div class="modal-header">
                        <h1 class="modal-title fs-5" id="editMembershipModalLabel">Edit Membership</h1>
                        <button type="button" class="btn-close" data-bs-dismiss="modal" aria-label="Close"></button>
                    </div>
                    <div class="modal-body">
                        <div class="mb-3">
                            <label for="editMembershipTeam" class="form-label">Team</label>
                            <select 
                                v-model="editingMembership.team_id" 
                                class="form-select" 
                                id="editMembershipTeam"
                            >
                                <option v-for="team in teams" :key="team.id" :value="team.id">
                                    {{ team.name }}
                                </option>
                            </select>
                        </div>
                        <div class="mb-3">
                            <label for="editMembershipLeague" class="form-label">League</label>
                            <select 
                                v-model="editingMembership.league_id" 
                                class="form-select" 
                                id="editMembershipLeague"
                            >
                                <option v-for="league in leagues" :key="league.id" :value="league.id">
                                    {{ league.name }}
                                </option>
                            </select>
                        </div>
                        <div class="mb-3">
                            <label for="editMembershipDate" class="form-label">Date Joined</label>
                            <input 
                                type="date" 
                                class="form-control" 
                                id="editMembershipDate"
                                v-model="editingMembership.date_joined"
                            >
                        </div>
                        <div class="mb-3 form-check">
                            <input 
                                type="checkbox" 
                                class="form-check-input" 
                                id="editMembershipActive"
                                v-model="editingMembership.still_active"
                            >
                            <label class="form-check-label" for="editMembershipActive">Still Active</label>
                        </div>
                    </div>
                    <div class="modal-footer">
                        <button type="button" class="btn btn-secondary" data-bs-dismiss="modal">Close</button>
                        <button type="button" class="btn btn-primary" @click="updateMembership()" data-bs-dismiss="modal">
                            Save Changes
                        </button>
                    </div>
                </div>
            </div>
        </div>
    </div>
</template>
  
<script>
    import Tabs from './components/Tabs.vue'
    import TeamTable from './components/TeamTable.vue'
    import LeagueTable from './components/LeagueTable.vue'
    import MembershipTable from './components/MembershipTable.vue'

    const baseUrl = 'http://localhost:8000'

    export default {
    components: {
        Tabs,
        TeamTable,
        LeagueTable,
        MembershipTable
    },
    data() {
        return {
            title: 'Football Information',
            teams: [],
            leagues: [],
            isEditingLeague: false,
            editingLeague: {
                id: null,
                name: '',
                location: ''
            },
            newLeague: {
                name: '',
                location: ''
            },
            newTeam: {
                name: '',
                city: '',
                captain: '',
                coach: '',
                year_founded: 1900
            },
            editingTeam: {
                id: null,
                name: '',
                city: '',
                captain: '',
                coach: '',
                year_founded: 1900
            },
            isEditingMembership: false,
            editingMembership: {
                id: null,
                team_id: null,
                league_id: null,
                still_active: true,
                date_joined: new Date().toISOString().split('T')[0]
            },
            newMembership: {
                team_id: null,
                league_id: null,
                still_active: true,
                date_joined: new Date().toISOString().split('T')[0]
            },
            memberships: []
        }
    },
    async mounted() {
        const [teamsResponse, leaguesResponse] = await Promise.all([
            fetch(`${baseUrl}/api/teams/`),
            fetch(`${baseUrl}/api/leagues/`)
        ]);

        const teamsData = await teamsResponse.json();
        const leaguesData = await leaguesResponse.json();

        this.teams = teamsData.teams;
        this.leagues = leaguesData.leagues;

        const membershipResponse = await fetch(`${baseUrl}/api/memberships/`);
        const membershipData = await membershipResponse.json();
        this.memberships = membershipData.memberships;
    },
    methods: {
        async deleteTeam(team) {
            if (confirm(`Are you sure you want to delete this team?`)) {
                try {
                    const response = await fetch(`${baseUrl}/api/teams/`, {
                        method: 'DELETE',
                        headers: {
                            'Content-Type': 'application/json'
                        },
                        body: JSON.stringify({ id: team.id })
                    });

                    if (!response.ok) {
                        throw new Error('Failed to delete team');
                    }

                    this.teams = this.teams.filter(c => c.id !== team.id);
                } catch (error) {
                    console.error('Error deleting team:', error);
                    alert('Failed to delete team');
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
            })
            const newTeam = await response.json()
            this.teams.push(newTeam)

            this.newTeam = {
                name: '',
                city: '',
                captain: '',
                coach: '',
                year_founded: 1900
            }
        },
        async createLeague() {
            try {
                const response = await fetch(`${baseUrl}/api/leagues/`, {
                    method: 'POST',
                    headers: {
                        'Content-Type': 'application/json'
                    },
                    body: JSON.stringify(this.newLeague)
                });

                if (!response.ok) {
                    throw new Error('Failed to create league');
                }

                const newLeague = await response.json();
                this.leagues.push(newLeague);

                this.newLeague = {
                    name: '',
                    location: ''
                };
            } catch (error) {
                console.error('Error creating league:', error);
                alert('Failed to create league');
            }
        },
        async deleteLeague(league) {
            if (confirm(`Are you sure you want to delete ${league.name}?`)) {
                try {
                    const response = await fetch(`${baseUrl}/api/leagues/`, {
                        method: 'DELETE',
                        headers: {
                            'Content-Type': 'application/json'
                        },
                        body: JSON.stringify({ id: league.id })
                    });

                    if (!response.ok) {
                        throw new Error('Failed to delete league');
                    }

                    this.leagues = this.leagues.filter(l => l.id !== league.id);
                } catch (error) {
                    console.error('Error deleting league:', error);
                    alert('Failed to delete league');
                }
            }
        },
        editTeam(team) {
            try {
                this.editingTeam = { ...team };
                const modal = new bootstrap.Modal(document.getElementById('editTeamModal'));
                modal.show();
            } catch (error) {
                console.error('Error showing modal:', error);
            }
        },
        editLeague(league) {
            try {
                this.isEditingLeague = true;
                this.editingLeague = { ...league };
                const modal = new bootstrap.Modal(document.getElementById('editLeagueModal'));
                modal.show();
            } catch (error) {
                console.error('Error showing modal:', error);
            }
        },
        async updateTeam() {
            try {
                const response = await fetch(`${baseUrl}/api/teams/`, {
                    method: 'PUT',
                    headers: {
                        'Content-Type': 'application/json'
                    },
                    body: JSON.stringify(this.editingTeam)
                });

                if (!response.ok) {
                    throw new Error('Failed to update team');
                }

                const updatedTeam = await response.json();
                const index = this.teams.findIndex(t => t.id === updatedTeam.id);
                if (index !== -1) {
                    this.teams[index] = updatedTeam;
                }
            } catch (error) {
                console.error('Error updating team:', error);
                alert('Failed to update team');
            }
        },
        async updateLeague() {
            try {
                const response = await fetch(`${baseUrl}/api/leagues/`, {
                    method: 'PUT',
                    headers: {
                        'Content-Type': 'application/json'
                    },
                    body: JSON.stringify(this.editingLeague)
                });

                if (!response.ok) {
                    throw new Error('Failed to update league');
                }

                const updatedLeague = await response.json();
                const index = this.leagues.findIndex(l => l.id === updatedLeague.id);
                if (index !== -1) {
                    this.leagues[index] = updatedLeague;
                }
            } catch (error) {
                console.error('Error updating league:', error);
                alert('Failed to update league');
            }
        },
        async createMembership() {
            try {
                if (!this.newMembership.team_id || !this.newMembership.league_id) {
                    throw new Error('Please select both a team and a league');
                }

                const response = await fetch(`${baseUrl}/api/memberships/`, {
                    method: 'POST',
                    headers: {
                        'Content-Type': 'application/json'
                    },
                    body: JSON.stringify({
                        team_id: this.newMembership.team_id,
                        league_id: this.newMembership.league_id,
                        still_active: this.newMembership.still_active,
                        date_joined: this.newMembership.date_joined
                    })
                });

                if (!response.ok) {
                    const contentType = response.headers.get('content-type');
                    if (contentType && contentType.includes('application/json')) {
                        const errorData = await response.json();
                        throw new Error(errorData.error || 'Failed to create membership');
                    } else {
                        throw new Error('Server error: Failed to create membership');
                    }
                }

                const newMembership = await response.json();
                this.memberships.push(newMembership);

                // Reset form
                this.newMembership = {
                    team_id: null,
                    league_id: null,
                    date_joined: new Date().toISOString().split('T')[0],
                    still_active: true
                };
            } catch (error) {
                console.error('Error creating membership:', error);
                alert(error.message);
            }
        },
        async deleteMembership(membership) {
            if (confirm(`Are you sure you want to delete this membership?`)) {
                try {
                    const response = await fetch(`${baseUrl}/api/memberships/`, {
                        method: 'DELETE',
                        headers: {
                            'Content-Type': 'application/json'
                        },
                        body: JSON.stringify({ id: membership.id })
                    });

                    if (!response.ok) {
                        throw new Error('Failed to delete membership');
                    }

                    this.memberships = this.memberships.filter(m => m.id !== membership.id);
                } catch (error) {
                    console.error('Error deleting membership:', error);
                    alert('Failed to delete membership');
                }
            }
        },

        editMembership(membership) {
            console.log('Editing membership:', membership); // Debug log
            this.editingMembership = {
                id: membership.id,
                team_id: membership.team.id,
                league_id: membership.league.id,
                still_active: membership.still_active,
                date_joined: membership.date_joined
            };
            
            // Use the bootstrap modal properly
            const modal = new bootstrap.Modal(document.getElementById('editMembershipModal'));
            modal.show();
        },

        async updateMembership() {
            try {
                const response = await fetch(`${baseUrl}/api/memberships/`, {
                    method: 'PUT',
                    headers: {
                        'Content-Type': 'application/json',
                        'Accept': 'application/json'  // Explicitly request JSON response
                    },
                    body: JSON.stringify({
                        id: this.editingMembership.id,
                        team_id: parseInt(this.editingMembership.team_id),
                        league_id: parseInt(this.editingMembership.league_id),
                        still_active: this.editingMembership.still_active,
                        date_joined: this.editingMembership.date_joined
                    })
                });

                let responseData;
                try {
                    responseData = await response.json();
                } catch (e) {
                    throw new Error('Server returned invalid JSON');
                }

                if (!response.ok) {
                    throw new Error(responseData.error || 'Failed to update membership');
                }

                // Update the membership in the list
                const index = this.memberships.findIndex(m => m.id === responseData.id);
                if (index !== -1) {
                    this.memberships[index] = responseData;
                    this.memberships = [...this.memberships];
                }

                // Close modal and reset form
                const modal = bootstrap.Modal.getInstance(document.getElementById('editMembershipModal'));
                if (modal) {
                    modal.hide();
                }

                // Reset the editing state
                this.editingMembership = {
                    id: null,
                    team_id: null,
                    league_id: null,
                    still_active: true,
                    date_joined: new Date().toISOString().split('T')[0]
                };
            } catch (error) {
                console.error('Error updating membership:', error);
                alert(error.message);
            }
        }
    }
}
</script>

<style scoped>
</style>