<template>
    <div>
        <ul class="nav nav-tabs mb-3" role="tablist">
            <li class="nav-item" role="presentation">
                <button
                    class="nav-link"
                    :class="{ active: activeTab === 'teams' }"
                    @click="activeTab = 'teams'"
                    type="button"
                    role="tab"
                >
                    Teams
                </button>
            </li>
            <li class="nav-item" role="presentation">
                <button
                    class="nav-link"
                    :class="{ active: activeTab === 'leagues' }"
                    @click="activeTab = 'leagues'"
                    type="button"
                    role="tab"
                >
                    Leagues
                </button>
            </li>
            <li class="nav-item" role="presentation">
                <button
                    class="nav-link"
                    :class="{ active: activeTab === 'memberships' }"
                    @click="activeTab = 'memberships'"
                    type="button"
                    role="tab"
                >
                    Memberships
                </button>
            </li>
        </ul>

        <div class="tab-content">
            <div v-show="activeTab === 'teams'" class="tab-pane fade show active">
                <slot name="teams"></slot>
            </div>
            <div v-show="activeTab === 'leagues'" class="tab-pane fade show active">
                <slot name="leagues"></slot>
            </div>
            <div v-show="activeTab === 'memberships'" class="tab-pane fade show active">
                <slot name="memberships"></slot>
            </div>
        </div>
    </div>
</template>

<script>
export default {
    data() {
        return {
            activeTab: 'teams'
        };
    }
};
</script>

<style scoped>
</style>