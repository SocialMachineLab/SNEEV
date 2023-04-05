<template>
  <div id="app">
    <div class="container-fluid">
      <div class="row">
        <div class="col-6">
          <div
            class="btn-toolbar"
            role="toolbar"
            aria-label="Toolbar with button groups"
          >
            <div class="btn-group mr-2" role="group" aria-label="First group">
              <!-- <button type="button" class="btn btn-success" v-on:click="init">Start Serve</button> -->
              <button type="button" class="btn btn-secondary" v-on:click="init">
                Init
              </button>
              <button type="button" class="btn btn-primary" v-on:click="login">
                Login
              </button>
              <button
                type="button"
                class="btn btn-danger"
                v-on:click="run_followings"
              >
                Run Followings
              </button>
              <button
                type="button"
                class="btn btn-warning"
                v-on:click="run_queries"
              >
                Run Queries
              </button>
              <button
                type="button"
                class="btn btn-info"
                v-on:click="next_session"
              >
                Next session
              </button>
            </div>
          </div>
        </div>
        <!-- <div class="col-1">
          <input v-model="config.session_id" />
          Time Interval
          <select>
            <option v-for="interval in config.intervals" v-bind:key="interval">{{ interval }}</option>
          </select>
        </div> -->
        <div class="col-6">
          <p>
            Session: {{ config.session_id }} | Max results:
            {{ config.max_results }} | interval:
            {{ config.interval / 1000 }}
          </p>
          <!-- <p>
            Current query:
            <strong v-if="config.queries">{{
              config.queries[query_iterator - 1]
            }}</strong>
          </p> -->
        </div>
      </div>

      <div class="row justify-center">
        <div class="col">
          <div class="row">
            <div
              class="col col-6"
              v-for="agent in this.agents"
              v-bind:key="agent.id"
            >
              <p>{{ agent.id }}</p>
              <img
                v-bind:src="agent.image_data"
                class="w-100 screenshot-image"
              />
              <div class="btn-group mr-2" role="group" aria-label="First group">
                <button
                  type="button"
                  class="btn btn-primary"
                  v-on:click="() => login_agent(agent)"
                >
                  Login
                </button>
                <!-- <button
                  type="button"
                  class="btn btn-danger"
                  v-on:click="() => follow_agent(agent, 'MomentsBrasil')"
                >
                  Follow
                </button> -->
              </div>

              <div class="row">
                <h2>Query List</h2>
                <ul class="list-group">
                  <li
                    class="list-group-item"
                    v-for="query in config.queries_status[agent.id]"
                    v-bind:key="query"
                  >
                    {{ query.query }}
                    <!-- <span v-for="agent in config.agents" v-bind:key="agent.id"> -->
                    <StatusIcon v-bind:status="query.status"></StatusIcon>
                    <!-- </span> -->
                  </li>
                </ul>
              </div>
              <div class="row">
                <h2>Profiles</h2>
                <ul class="list-group">
                  <li
                    class="list-group-item"
                    v-for="profile in config.profiles_status[agent.id]"
                    v-bind:key="profile.profile"
                  >
                    {{ profile.profile }}
                    <StatusIcon v-bind:status="profile.status"></StatusIcon>
                  </li>
                </ul>
              </div>
            </div>
          </div>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
const init_config = session_id => {
  let _config = require(`./session_configs/twitter/${session_id}.json`);

  let new_config = {
    ..._config,
    queries_status: {},
    profiles_status: {},
    login_status: {},
    agents: { ..._config.agents }
  };

  for (let agent_key in _config.agents) {
    new_config.login_status[agent_key] = false;
    new_config.profiles_status[agent_key] = [];
    new_config.queries_status[agent_key] = [];
    for (let profile of _config.agents[agent_key].profiles) {
      new_config.profiles_status[agent_key].push({
        profile,
        status: "idle"
      });
    }
    for (let query of _config.agents[agent_key].queries) {
      new_config.queries_status[agent_key].push({
        query,
        status: "idle"
      });
    }
  }
  return new_config;
};

import StatusIcon from "./components/StatusIcon.vue";

export default {
  name: "app",
  data: () => ({
    sessions: [
      // '_test1',
      // '_test2',
      // 'r_000_p',
      // "tumblr",
      // "reddit-language",
      // "reddita"
// "twitter-abtesting2",
// "twitter-abtesting"
// 'reddita'
// 'reddit-po1',
// "twitter-po2"
// "reddit-po-multi copy"
// "twitter-follow0",
// "twitter-follow1",
// "twitter-follow2",
// "twitter-follow3",
// "twitter-follow4",
// "twitter-follow5",
// "twitter-follow6",
// "twitter-follow7",
// "twitter-follow8",
// "twitter-follow9",
// "twitter-follow10",
// "twitter-follow11",
// "twitter-follow12",
// "twitter-follow13",
// "twitter-follow14",
// "twitter-follow15",
// "twitter-follow16",
// "twitter-follow17",
// "twitter-follow18",
// "twitter-follow19",
// "twitter-follow20",
// "twitter-follow21",
// "twitter-follow22",
// "twitter-follow23",
// "twitter-follow24",
// "twitter-follow25",
// "twitter-follow26",
// "twitter-follow27",
// "twitter-follow28",
// "twitter-follow29",
// "twitter-follow30",
"twitter-follow31",
"twitter-follow32",
"twitter-follow33",
"twitter-follow34",
"twitter-follow35",
"twitter-follow36",
"twitter-follow37",
"twitter-follow38",
"twitter-follow39",
"twitter-follow40"


// "twitter-follow_0",
// "twitter-follow_1",
// "twitter-follow_2",
// "twitter-follow_3",
// "twitter-follow_4",
// "twitter-follow_5",
// "twitter-follow_6",
// "twitter-follow_7",
// "twitter-follow_8",
// "twitter-follow_9",
// "twitter-follow_10",
// "twitter-follow_11",
// "twitter-follow_12",
// "twitter-follow_13",
// "twitter-follow_14",
// "twitter-follow_15",
// "twitter-follow_16",
// "twitter-follow_17",
// "twitter-follow_18",
// "twitter-follow_19",
// "twitter-follow_20",
// "twitter-follow_21",
// "twitter-follow_22",
// "twitter-follow_23"


// "twitter-follow_new_0",
// "twitter-follow_new_1",
// "twitter-follow_new_2",
// "twitter-follow_new_3",
// "twitter-follow_new_4",
// "twitter-follow_new_5",
// "twitter-follow_new_6",
// "twitter-follow_new_7",
// "twitter-follow_new_8",
// "twitter-follow_new_9",
// "twitter-follow_new_10",
// "twitter-follow_new_11",
// "twitter-follow_new_12",
// "twitter-follow_new_13",
// "twitter-follow_new_14",
// "twitter-follow_new_15",
// "twitter-follow_new_16",
// "twitter-follow_new_17",
// "twitter-follow_new_18",
// "twitter-follow_new_19",
// "twitter-follow_new_20",
// "twitter-follow_new_21",
// "twitter-follow_new_22",
// "twitter-follow_new_23",
// "twitter-follow_new_24",
// "twitter-follow_new_25",
// "twitter-follow_new_26",
// "twitter-follow_new_27",
// "twitter-follow_new_28",
// "twitter-follow_new_29",
// "twitter-follow_new_30",
// "twitter-follow_new_31",
// "twitter-follow_new_32",
// "twitter-follow_new_33",
// "twitter-follow_new_34",
// "twitter-follow_new_35",
// "twitter-follow_new_36",
// "twitter-follow_new_37",
// "twitter-follow_new_38",
// "twitter-follow_new_39"

// 'reddit-carry1-1',
//  'reddit-carry1-2',
//  'reddit-carry1-3',
//  'reddit-carry1-4',
//  'reddit-carry1-5',
//  'reddit-carry1-6',
//  'reddit-carry1-7',
//  'reddit-carry1-8',
//  'reddit-carry1-9',
//  'reddit-carry1-10',
//  'reddit-carry1-11',
//  'reddit-carry1-12',
//  'reddit-carry1-13',
//  'reddit-carry1-14',
//  'reddit-carry1-15',
//  'reddit-carry1-16',
//  'reddit-carry1-17',
//  'reddit-carry1-18',
//  'reddit-carry1-19',
//  'reddit-carry1-20',
//  'reddit-carry2-1',
//  'reddit-carry2-2',
//  'reddit-carry2-3',
//  'reddit-carry2-4',
//  'reddit-carry2-5',
//  'reddit-carry2-6',
//  'reddit-carry2-7',
//  'reddit-carry2-8',
//  'reddit-carry2-9',
//  'reddit-carry2-10',
//  'reddit-carry2-11',
//  'reddit-carry2-12',
//  'reddit-carry2-13',
//  'reddit-carry2-14',
//  'reddit-carry2-15',
//  'reddit-carry2-16',
//  'reddit-carry2-17',
//  'reddit-carry2-18',
// --
//  'reddit-carry2-19',
//  'reddit-carry2-20',
//  'reddit-carry3-1',
//  'reddit-carry3-2',
//  'reddit-carry3-3',
//  'reddit-carry3-4',
//  'reddit-carry3-5',
//  'reddit-carry3-6',
//  'reddit-carry3-7',
//  'reddit-carry3-8',
//  'reddit-carry3-9',
//  'reddit-carry3-10',
//  'reddit-carry3-11',
//  'reddit-carry3-12',
//  'reddit-carry3-13',
//  'reddit-carry3-14',
//  'reddit-carry3-15',
//  'reddit-carry3-16',
//  'reddit-carry3-17',
//  'reddit-carry3-18',
//  'reddit-carry3-19',
//  'reddit-carry3-20',
//  'reddit-carry5-1',
//  'reddit-carry5-2',
//  'reddit-carry5-3',
//  'reddit-carry5-4',
//  'reddit-carry5-5',
//  'reddit-carry5-6',
//  'reddit-carry5-7',
//  'reddit-carry5-8',
//  'reddit-carry5-9',
//  'reddit-carry5-10',
//  'reddit-carry5-11',
//  'reddit-carry5-12',
//  'reddit-carry5-13',
//  'reddit-carry5-14',
//  'reddit-carry5-15',
//  'reddit-carry5-16',
//  'reddit-carry5-17',
//  'reddit-carry5-18',
//  'reddit-carry5-19',
//  'reddit-carry5-20',
//  'reddit-carry6-1',
//  'reddit-carry6-2',
//  'reddit-carry6-3',
//  'reddit-carry6-4',
//  'reddit-carry6-5',
//  'reddit-carry6-6',
//  'reddit-carry6-7',
//  'reddit-carry6-8',
//  'reddit-carry6-9',
//  'reddit-carry6-10',
//  'reddit-carry6-11',
//  'reddit-carry6-12',
//  'reddit-carry6-13',
//  'reddit-carry6-14',
//  'reddit-carry6-15',
//  'reddit-carry6-16',
//  'reddit-carry6-17',
//  'reddit-carry6-18',
//  'reddit-carry6-19',
//  'reddit-carry6-20',
//  'reddit-carry7-1',
//  'reddit-carry7-2',
//  'reddit-carry7-3',
//  'reddit-carry7-4',
//  'reddit-carry7-5',
//  'reddit-carry7-6',
//  'reddit-carry7-7',
//  'reddit-carry7-8',
//  'reddit-carry7-9',
//  'reddit-carry7-10',
//  'reddit-carry7-11',
//  'reddit-carry7-12',
//  'reddit-carry7-13',
//  'reddit-carry7-14',
//  'reddit-carry7-15',
//  'reddit-carry7-16',
//  'reddit-carry7-17',
//  'reddit-carry7-18',
//  'reddit-carry7-19',
//  'reddit-carry7-20',
//  'reddit-carry8-1',
//  'reddit-carry8-2',
//  'reddit-carry8-3',
//  'reddit-carry8-4',
//  'reddit-carry8-5',
//  'reddit-carry8-6',
//  'reddit-carry8-7',
//  'reddit-carry8-8',
//  'reddit-carry8-9',
//  'reddit-carry8-10',
//  'reddit-carry8-11',
//  'reddit-carry8-12',
//  'reddit-carry8-13',
//  'reddit-carry8-14',
//  'reddit-carry8-15',
//  'reddit-carry8-16',
//  'reddit-carry8-17',
//  'reddit-carry8-18',
//  'reddit-carry8-19',
//  'reddit-carry8-20',
//  'reddit-carry9-1',
//  'reddit-carry9-2',
//  'reddit-carry9-3',
//  'reddit-carry9-4',
//  'reddit-carry9-5',
//  'reddit-carry9-6',
//  'reddit-carry9-7',
//  'reddit-carry9-8',
//  'reddit-carry9-9',
//  'reddit-carry9-10',
//  'reddit-carry9-11',
//  'reddit-carry9-12',
//  'reddit-carry9-13',
//  'reddit-carry9-14',
//  'reddit-carry9-15',
//  'reddit-carry9-16',
//  'reddit-carry9-17',
//  'reddit-carry9-18',
//  'reddit-carry9-19',
//  'reddit-carry9-20',
//  'reddit-carry10-1',
//  'reddit-carry10-2',
//  'reddit-carry10-3',
//  'reddit-carry10-4',
//  'reddit-carry10-5',
//  'reddit-carry10-6',
//  'reddit-carry10-7',
//  'reddit-carry10-8',
//  'reddit-carry10-9',
//  'reddit-carry10-10',
//  'reddit-carry10-11',
//  'reddit-carry10-12',
//  'reddit-carry10-13',
//  'reddit-carry10-14',
//  'reddit-carry10-15',
//  'reddit-carry10-16',
//  'reddit-carry10-17',
//  'reddit-carry10-18',
//  'reddit-carry10-19',
//  'reddit-carry10-20',
//  'reddit-carry11-1',
//  'reddit-carry11-2',
//  'reddit-carry11-3',
//  'reddit-carry11-4',
//  'reddit-carry11-5',
//  'reddit-carry11-6',
//  'reddit-carry11-7',
//  'reddit-carry11-8',
//  'reddit-carry11-9',
//  'reddit-carry11-10',
//  'reddit-carry11-11',
//  'reddit-carry11-12',
//  'reddit-carry11-13',
//  'reddit-carry11-14',
//  'reddit-carry11-15',
//  'reddit-carry11-16',
//  'reddit-carry11-17',
//  'reddit-carry11-18',
//  'reddit-carry11-19',
//  'reddit-carry11-20',
//  'reddit-carry12-1',
//  'reddit-carry12-2',
//  'reddit-carry12-3',
//  'reddit-carry12-4',
//  'reddit-carry12-5',
//  'reddit-carry12-6',
//  'reddit-carry12-7',
//  'reddit-carry12-8',
//  'reddit-carry12-9',
//  'reddit-carry12-10',
//  'reddit-carry12-11',
//  'reddit-carry12-12',
//  'reddit-carry12-13',
//  'reddit-carry12-14',
//  'reddit-carry12-15',
//  'reddit-carry12-16',
//  'reddit-carry12-17',
//  'reddit-carry12-18',
//  'reddit-carry12-19',
//  'reddit-carry12-20',
//  'reddit-carry14-1',
//  'reddit-carry14-2',
//  'reddit-carry14-3',
//  'reddit-carry14-4',
//  'reddit-carry14-5',
//  'reddit-carry14-6',
//  'reddit-carry14-7',
//  'reddit-carry14-8',
//  'reddit-carry14-9',
//  'reddit-carry14-10',
//  'reddit-carry14-11',
//  'reddit-carry14-12',
//  'reddit-carry14-13',
//  'reddit-carry14-14',
//  'reddit-carry14-15',
//  'reddit-carry14-16',
//  'reddit-carry14-17',
//  'reddit-carry14-18',
//  'reddit-carry14-19',
//  'reddit-carry14-20',
//  'reddit-carry15-1',
//  'reddit-carry15-2',
//  'reddit-carry15-3',
//  'reddit-carry15-4',
//  'reddit-carry15-5',
//  'reddit-carry15-6',
//  'reddit-carry15-7',
//  'reddit-carry15-8',
//  'reddit-carry15-9',
//  'reddit-carry15-10',
//  'reddit-carry15-11',
//  'reddit-carry15-12',
//  'reddit-carry15-13',
//  'reddit-carry15-14',
//  'reddit-carry15-15',
//  'reddit-carry15-16',
//  'reddit-carry15-17',
//  'reddit-carry15-18',
//  'reddit-carry15-19',
//  'reddit-carry15-20',
//  'reddit-carry17-1',
//  'reddit-carry17-2',
//  'reddit-carry17-3',
//  'reddit-carry17-4',
//  'reddit-carry17-5',
//  'reddit-carry17-6',
//  'reddit-carry17-7',
//  'reddit-carry17-8',
//  'reddit-carry17-9',
//  'reddit-carry17-10',
//  'reddit-carry17-11',
//  'reddit-carry17-12',
//  'reddit-carry17-13',
//  'reddit-carry17-14',
//  'reddit-carry17-15',
//  'reddit-carry17-16',
//  'reddit-carry17-17',
//  'reddit-carry17-18',
//  'reddit-carry17-19',
//  'reddit-carry17-20',
//  'reddit-carry18-1',
//  'reddit-carry18-2',
//  'reddit-carry18-3',
//  'reddit-carry18-4',
//  'reddit-carry18-5',
//  'reddit-carry18-6',
//  'reddit-carry18-7',
//  'reddit-carry18-8',
//  'reddit-carry18-9',
//  'reddit-carry18-10',
//  'reddit-carry18-11',
//  'reddit-carry18-12',
//  'reddit-carry18-13',
//  'reddit-carry18-14',
//  'reddit-carry18-15',
//  'reddit-carry18-16',
//  'reddit-carry18-17',
//  'reddit-carry18-18',
//  'reddit-carry18-19',
//  'reddit-carry18-20',
//  'reddit-carry19-1',
//  'reddit-carry19-2',
//  'reddit-carry19-3',
//  'reddit-carry19-4',
//  'reddit-carry19-5',
//  'reddit-carry19-6',
//  'reddit-carry19-7',
//  'reddit-carry19-8',
//  'reddit-carry19-9',
//  'reddit-carry19-10',
//  'reddit-carry19-11',
//  'reddit-carry19-12',
//  'reddit-carry19-13',
//  'reddit-carry19-14',
//  'reddit-carry19-15',
//  'reddit-carry19-16',
//  'reddit-carry19-17',
//  'reddit-carry19-18',
//  'reddit-carry19-19',
//  'reddit-carry19-20',
//  'reddit-carry20-1',
//  'reddit-carry20-2',
//  'reddit-carry20-3',
//  'reddit-carry20-4',
//  'reddit-carry20-5',
//  'reddit-carry20-6',
//  'reddit-carry20-7',
//  'reddit-carry20-8',
//  'reddit-carry20-9',
//  'reddit-carry20-10',
//  'reddit-carry20-11',
//  'reddit-carry20-12',
//  'reddit-carry20-13',
//  'reddit-carry20-14',
//  'reddit-carry20-15',
//  'reddit-carry20-16',
//  'reddit-carry20-17',
//  'reddit-carry20-18',
//  'reddit-carry20-19',
//  'reddit-carry20-20',
//  'reddit-carry21-1',
//  'reddit-carry21-2',
//  'reddit-carry21-3',
//  'reddit-carry21-4',
//  'reddit-carry21-5',
//  'reddit-carry21-6',
//  'reddit-carry21-7',
//  'reddit-carry21-8',
//  'reddit-carry21-9',
//  'reddit-carry21-10',
//  'reddit-carry21-11',
//  'reddit-carry21-12',
//  'reddit-carry21-13',
//  'reddit-carry21-14',
//  'reddit-carry21-15',
//  'reddit-carry21-16',
//  'reddit-carry21-17',
//  'reddit-carry21-18',
//  'reddit-carry21-19',
//  'reddit-carry21-20',
//  'reddit-carry22-1',
//  'reddit-carry22-2',
//  'reddit-carry22-3',
//  'reddit-carry22-4',
//  'reddit-carry22-5',
//  'reddit-carry22-6',
//  'reddit-carry22-7',
//  'reddit-carry22-8',
//  'reddit-carry22-9',
//  'reddit-carry22-10',
//  'reddit-carry22-11',
//  'reddit-carry22-12',
//  'reddit-carry22-13',
//  'reddit-carry22-14',
//  'reddit-carry22-15',
//  'reddit-carry22-16',
//  'reddit-carry22-17',
//  'reddit-carry22-18',
//  'reddit-carry22-19',
//  'reddit-carry22-20',
//  'reddit-carry23-1',
//  'reddit-carry23-2',
//  'reddit-carry23-3',
//  'reddit-carry23-4',
//  'reddit-carry23-5',
//  'reddit-carry23-6',
//  'reddit-carry23-7',
//  'reddit-carry23-8',
//  'reddit-carry23-9',
//  'reddit-carry23-10',
//  'reddit-carry23-11',
//  'reddit-carry23-12',
//  'reddit-carry23-13',
//  'reddit-carry23-14',
//  'reddit-carry23-15',
//  'reddit-carry23-16',
//  'reddit-carry23-17',
//  'reddit-carry23-18',
//  'reddit-carry23-19',
//  'reddit-carry23-20',
//  'reddit-carry24-1',
//  'reddit-carry24-2',
//  'reddit-carry24-3',
//  'reddit-carry24-4',
//  'reddit-carry24-5',
//  'reddit-carry24-6',
//  'reddit-carry24-7',
//  'reddit-carry24-8',
//  'reddit-carry24-9',
//  'reddit-carry24-10',
//  'reddit-carry24-11',
//  'reddit-carry24-12',
//  'reddit-carry24-13',
//  'reddit-carry24-14',
//  'reddit-carry24-15',
//  'reddit-carry24-16',
//  'reddit-carry24-17',
//  'reddit-carry24-18',
//  'reddit-carry24-19',
//  'reddit-carry24-20',
//  'reddit-carry25-1',
//  'reddit-carry25-2',
//  'reddit-carry25-3',
//  'reddit-carry25-4',
//  'reddit-carry25-5',
//  'reddit-carry25-6',
//  'reddit-carry25-7',
//  'reddit-carry25-8',
//  'reddit-carry25-9',
//  'reddit-carry25-10',
//  'reddit-carry25-11',
//  'reddit-carry25-12',
//  'reddit-carry25-13',
//  'reddit-carry25-14',
//  'reddit-carry25-15',
//  'reddit-carry25-16',
//  'reddit-carry25-17',
//  'reddit-carry25-18',
//  'reddit-carry25-19',
//  'reddit-carry25-20',
//  'reddit-carry26-1',
//  'reddit-carry26-2',
//  'reddit-carry26-3',
//  'reddit-carry26-4',
//  'reddit-carry26-5',
//  'reddit-carry26-6',
//  'reddit-carry26-7',
//  'reddit-carry26-8',
//  'reddit-carry26-9',
//  'reddit-carry26-10',
//  'reddit-carry26-11',
//  'reddit-carry26-12',
//  'reddit-carry26-13',
//  'reddit-carry26-14',
//  'reddit-carry26-15',
//  'reddit-carry26-16',
//  'reddit-carry26-17',
//  'reddit-carry26-18',
//  'reddit-carry26-19',
//  'reddit-carry26-20',
//  'reddit-carry27-1',
//  'reddit-carry27-2',
//  'reddit-carry27-3',
//  'reddit-carry27-4',
//  'reddit-carry27-5',
//  'reddit-carry27-6',
//  'reddit-carry27-7',
//  'reddit-carry27-8',
//  'reddit-carry27-9',
//  'reddit-carry27-10',
//  'reddit-carry27-11',
//  'reddit-carry27-12',
//  'reddit-carry27-13',
//  'reddit-carry27-14',
//  'reddit-carry27-15',
//  'reddit-carry27-16',
//  'reddit-carry27-17',
//  'reddit-carry27-18',
//  'reddit-carry27-19',
//  'reddit-carry27-20',
//  'reddit-carry28-1',
//  'reddit-carry28-2',
//  'reddit-carry28-3',
//  'reddit-carry28-4',
//  'reddit-carry28-5',
//  'reddit-carry28-6',
//  'reddit-carry28-7',
//  'reddit-carry28-8',
//  'reddit-carry28-9',
//  'reddit-carry28-10',
//  'reddit-carry28-11',
//  'reddit-carry28-12',
//  'reddit-carry28-13',
//  'reddit-carry28-14',
//  'reddit-carry28-15',
//  'reddit-carry28-16',
//  'reddit-carry28-17',
//  'reddit-carry28-18',
//  'reddit-carry28-19',
//  'reddit-carry28-20'

      //  'reddit-carry18-1',
      //  'reddit-carry18-2',
      //  'reddit-carry18-3',
      //  'reddit-carry18-4',
      //  'reddit-carry18-5',
      //  'reddit-carry18-6',
      //  'reddit-carry18-7',
      //  'reddit-carry18-8',
      //  'reddit-carry18-9',
      //  'reddit-carry18-10',
      //  'reddit-carry18-11',
      //  'reddit-carry18-12',
      //  'reddit-carry18-13',
      //  'reddit-carry18-14',
      //  'reddit-carry18-15',
      //  'reddit-carry18-16',
      //  'reddit-carry18-17',
      //  'reddit-carry18-18',
      //  'reddit-carry18-19',
      //  'reddit-carry18-20',
      //  'reddit-carry20-1',
      //  'reddit-carry20-2',
      //  'reddit-carry20-3',
      //  'reddit-carry20-4',
      //  'reddit-carry20-5',
      //  'reddit-carry20-6',
      //  'reddit-carry20-7',
      //  'reddit-carry20-8',
      //  'reddit-carry20-9',
      //  'reddit-carry20-10',
      //  'reddit-carry20-11',
      //  'reddit-carry20-12',
      //  'reddit-carry20-13',
      //  'reddit-carry20-14',
      //  'reddit-carry20-15',
      //  'reddit-carry20-16',
      //  'reddit-carry20-17',
      //  'reddit-carry20-18',
      //  'reddit-carry20-19',
      //  'reddit-carry20-20',
      //  'reddit-carry26-1',
      //  'reddit-carry26-2',
      //  'reddit-carry26-3',
      //  'reddit-carry26-4',
      //  'reddit-carry26-5',
      //  'reddit-carry26-6',
      //  'reddit-carry26-7',
      //  'reddit-carry26-8',
      //  'reddit-carry26-9',
      //  'reddit-carry26-10',
      //  'reddit-carry26-11',
      //  'reddit-carry26-12',
      //  'reddit-carry26-13',
      //  'reddit-carry26-14',
      //  'reddit-carry26-15',
      //  'reddit-carry26-16',
      //  'reddit-carry26-17',
      //  'reddit-carry26-18',
      //  'reddit-carry26-19',
      //  'reddit-carry26-20',
      //  'reddit-carry27-1',
      //  'reddit-carry27-2',
      //  'reddit-carry27-3',
      //  'reddit-carry27-4',
      //  'reddit-carry27-5',
      //  'reddit-carry27-6',
      //  'reddit-carry27-7',
      //  'reddit-carry27-8',
      //  'reddit-carry27-9',
      //  'reddit-carry27-10',
      //  'reddit-carry27-11',
      //  'reddit-carry27-12',
      //  'reddit-carry27-13',
      //  'reddit-carry27-14',
      //  'reddit-carry27-15',
      //  'reddit-carry27-16',
      //  'reddit-carry27-17',
      //  'reddit-carry27-18',
      //  'reddit-carry27-19',
      //  'reddit-carry27-20',
    // "redditac"
    // "tumblr"
      // "reddita2"
      //       "reddita1",
      // "reddita2",
      // "reddita3",
      // "reddita4",
      // "reddita5",
      // "reddita6",
      // "reddita7",
      // "reddita8",
      // "reddita9",
      // "reddita10",
      // "reddita11",
      // "reddita12",
      // "reddita13",
      // "reddita14",
      // "reddita15",
      // "reddita16",
      // "reddita17",
      // "reddita18",
      // "reddita19",
      // "reddita20",
      // "reddita21",
      // "reddita22",
      // "reddita23",
      // "reddita24",
      // "reddita25",
      // "reddita26",
      // "reddita27",
      // "reddita28",
      // "reddita29",
      // "reddita30",
      // "reddita31",
      // "reddita32",
      // "reddita33",
      // "reddita34",
      // "reddita35",
      // "reddita36",
      // "reddita37",
      // "reddita38",
      // "reddita39",
      // "reddita40"
      // "tumblr",
      // "tumblr copy",
      // "tumblr copy 2",
      // "tumblr copy 3",
      // "tumblr copy 4",
      // "tumblr copy 5",
      // "tumblr copy 6",
      // "tumblr copy 7",
      // "tumblr copy 8",
      // "tumblr copy 9",
      // "tumblr copy 10",
      // "tumblr copy 11",
      // "tumblr copy 12",
      // "tumblr copy 13",
      // "tumblr copy 14"
      // "twitter"
      // 'r_010_p',
      // 'r_020_p',
      // 'r_030_p',
      // 'r_040_p',
      // 'r_050_p',
      // 'r_070_p',
      // 'r_080_p',
      // 'r_090_p',
      // 'r_100_p',
      // 'twittercookie1',
      // 'twittercookie2'
      // 'twitter-language',
      // 'twitter-language2'
      // "reddita"

      // 'tumblr-carry1-1',
      //  'tumblr-carry1-2',
      //  'tumblr-carry1-3',
      //  'tumblr-carry1-4',
      //  'tumblr-carry1-5',
      //  'tumblr-carry1-6',
      //  'tumblr-carry1-7',
      //  'tumblr-carry1-8',
      //  'tumblr-carry1-9',
      //  'tumblr-carry1-10',
      //  'tumblr-carry1-11',
      //  'tumblr-carry1-12',
      //  'tumblr-carry1-13',
      //  'tumblr-carry1-14',
      //  'tumblr-carry1-15',
      //  'tumblr-carry1-16',
      //  'tumblr-carry1-17',
      //  'tumblr-carry1-18',
      //  'tumblr-carry1-19',
      //  'tumblr-carry1-20',   
      //  'tumblr-carry8-1',
      //  'tumblr-carry8-2',
      //  'tumblr-carry8-3',
      //  'tumblr-carry8-4',
      //  'tumblr-carry8-5',
      //  'tumblr-carry8-6',
      //  'tumblr-carry8-7',
      //  'tumblr-carry8-8',




      //  'tumblr-carry8-9',
      //  'tumblr-carry8-10',
      //  'tumblr-carry8-11',
      //  'tumblr-carry8-12',
      //  'tumblr-carry8-13',
      //  'tumblr-carry8-14',
      //  'tumblr-carry8-15',
      //  'tumblr-carry8-16',
      //  'tumblr-carry8-17',
      //  'tumblr-carry8-18',
      //  'tumblr-carry8-19',
      //  'tumblr-carry8-20',
      //  'tumblr-carry10-1',
      //  'tumblr-carry10-2',
      //  'tumblr-carry10-3',
      //  'tumblr-carry10-4',
      //  'tumblr-carry10-5',
      //  'tumblr-carry10-6',
      //  'tumblr-carry10-7',
      //  'tumblr-carry10-8',
      //  'tumblr-carry10-9',
      //  'tumblr-carry10-10',
      //  'tumblr-carry10-11',
      //  'tumblr-carry10-12',
      //  'tumblr-carry10-13',
      //  'tumblr-carry10-14',
      //  'tumblr-carry10-15',
      //  'tumblr-carry10-16',
      //  'tumblr-carry10-17',
      //  'tumblr-carry10-18',
      //  'tumblr-carry10-19',
      //  'tumblr-carry10-20',
      //  'tumblr-carry18-1',
      //  'tumblr-carry18-2',
      //  'tumblr-carry18-3',
      //  'tumblr-carry18-4',
      //  'tumblr-carry18-5',
      //  'tumblr-carry18-6',
      //  'tumblr-carry18-7',
      //  'tumblr-carry18-8',
      //  'tumblr-carry18-9',
      //  'tumblr-carry18-10',
      //  'tumblr-carry18-11',
      //  'tumblr-carry18-12',
      //  'tumblr-carry18-13',
      //  'tumblr-carry18-14',
      //  'tumblr-carry18-15',
      //  'tumblr-carry18-16',
      //  'tumblr-carry18-17',
      //  'tumblr-carry18-18',
      //  'tumblr-carry18-19',
      //  'tumblr-carry18-20',
      //  'tumblr-carry20-1',
      //  'tumblr-carry20-2',
      //  'tumblr-carry20-3',
      //  'tumblr-carry20-4',
      //  'tumblr-carry20-5',
      //  'tumblr-carry20-6',
      //  'tumblr-carry20-7',
      //  'tumblr-carry20-8',
      //  'tumblr-carry20-9',
      //  'tumblr-carry20-10',
      //  'tumblr-carry20-11',
      //  'tumblr-carry20-12',
      //  'tumblr-carry20-13',
      //  'tumblr-carry20-14',
      //  'tumblr-carry20-15',
      //  'tumblr-carry20-16',
      //  'tumblr-carry20-17',
      //  'tumblr-carry20-18',
      //  'tumblr-carry20-19',
      //  'tumblr-carry20-20',
      //  'tumblr-carry22-1',
      //  'tumblr-carry22-2',
      //  'tumblr-carry22-3',
      //  'tumblr-carry22-4',
      //  'tumblr-carry22-5',
      //  'tumblr-carry22-6',
      //  'tumblr-carry22-7',
      //  'tumblr-carry22-8',
      //  'tumblr-carry22-9',
      //  'tumblr-carry22-10',
      //  'tumblr-carry22-11',
      //  'tumblr-carry22-12',
      //  'tumblr-carry22-13',
      //  'tumblr-carry22-14',
      //  'tumblr-carry22-15',
      //  'tumblr-carry22-16',
      //  'tumblr-carry22-17',
      //  'tumblr-carry22-18',
      //  'tumblr-carry22-19',
      //  'tumblr-carry22-20',
      //  'tumblr-carry23-1',
      //  'tumblr-carry23-2',
      //  'tumblr-carry23-3',
      //  'tumblr-carry23-4',
      //  'tumblr-carry23-5',
      //  'tumblr-carry23-6',
      //  'tumblr-carry23-7',
      //  'tumblr-carry23-8',
      //  'tumblr-carry23-9',
      //  'tumblr-carry23-10',
      //  'tumblr-carry23-11',
      //  'tumblr-carry23-12',
      //  'tumblr-carry23-13',
      //  'tumblr-carry23-14',
      //  'tumblr-carry23-15',
      //  'tumblr-carry23-16',
      //  'tumblr-carry23-17',
      //  'tumblr-carry23-18',
      //  'tumblr-carry23-19',
      //  'tumblr-carry23-20',
     
      //  'tumblr-carry27-1',
      //  'tumblr-carry27-2',
      //  'tumblr-carry27-3',
      //  'tumblr-carry27-4',
      //  'tumblr-carry27-5',
      //  'tumblr-carry27-6',
      //  'tumblr-carry27-7',
      //  'tumblr-carry27-8',
      //  'tumblr-carry27-9',
      //  'tumblr-carry27-10',
      //  'tumblr-carry27-11',
      //  'tumblr-carry27-12',
      //  'tumblr-carry27-13',
      //  'tumblr-carry27-14',
      //  'tumblr-carry27-15',
      //  'tumblr-carry27-16',
      //  'tumblr-carry27-17',
      //  'tumblr-carry27-18',
      //  'tumblr-carry27-19',
      //  'tumblr-carry27-20',
      //  'tumblr-carry28-1',
      //  'tumblr-carry28-2',
      //  'tumblr-carry28-3',
      //  'tumblr-carry28-4',
      //  'tumblr-carry28-5',
      //  'tumblr-carry28-6',
      //  'tumblr-carry28-7',
      //  'tumblr-carry28-8',
      //  'tumblr-carry28-9',
      //  'tumblr-carry28-10',
      //  'tumblr-carry28-11',
      //  'tumblr-carry28-12',
      //  'tumblr-carry28-13',
      //  'tumblr-carry28-14',
      //  'tumblr-carry28-15',
      //  'tumblr-carry28-16',
      //  'tumblr-carry28-17',
      //  'tumblr-carry28-18',
      //  'tumblr-carry28-19',
      //  'tumblr-carry28-20'



// 'twitter-carry1-1',
//  'twitter-carry1-2',
//  'twitter-carry1-3',
//  'twitter-carry1-4',
//  'twitter-carry1-5',
//  'twitter-carry1-6',
//  'twitter-carry1-7',
//  'twitter-carry1-8',
//  'twitter-carry1-9',
//  'twitter-carry1-10',
//  'twitter-carry1-11',
//  'twitter-carry1-12',
//  'twitter-carry1-13',
//  'twitter-carry1-14',
//  'twitter-carry1-15',
//  'twitter-carry1-16',
//  'twitter-carry1-17',
//  'twitter-carry1-18',
//  'twitter-carry1-19',
//  'twitter-carry1-20',
//  'twitter-carry2-1',
//  'twitter-carry2-2',
//  'twitter-carry2-3',
//  'twitter-carry2-4',
//  'twitter-carry2-5',
//  'twitter-carry2-6',
//  'twitter-carry2-7',
//  'twitter-carry2-8',
//  'twitter-carry2-9',
//  'twitter-carry2-10',
//  'twitter-carry2-11',
//  'twitter-carry2-12',
//  'twitter-carry2-13',
//  'twitter-carry2-14',
//  'twitter-carry2-15',
//  'twitter-carry2-16',
//  'twitter-carry2-17',
//  'twitter-carry2-18',
//  'twitter-carry2-19',
//  'twitter-carry2-20',
//  'twitter-carry3-1',
//  'twitter-carry3-2',
//  'twitter-carry3-3',
//  'twitter-carry3-4',
//  'twitter-carry3-5',
//  'twitter-carry3-6',
//  'twitter-carry3-7',
//  'twitter-carry3-8',
//  'twitter-carry3-9',
//  'twitter-carry3-10',
//  'twitter-carry3-11',
//  'twitter-carry3-12',
//  'twitter-carry3-13',
//  'twitter-carry3-14',
//  'twitter-carry3-15',
//  'twitter-carry3-16',
//  'twitter-carry3-17',
//  'twitter-carry3-18',
//  'twitter-carry3-19',
//  'twitter-carry3-20',
//  'twitter-carry4-1',
//  'twitter-carry4-2',
//  'twitter-carry4-3',
//  'twitter-carry4-4',
//  'twitter-carry4-5',
//  'twitter-carry4-6',
//  'twitter-carry4-7',
//  'twitter-carry4-8',
//  'twitter-carry4-9',
//  'twitter-carry4-10',
//  'twitter-carry4-11',
//  'twitter-carry4-12',
//  'twitter-carry4-13',
//  'twitter-carry4-14',
//  'twitter-carry4-15',
//  'twitter-carry4-16',
//  'twitter-carry4-17',
//  'twitter-carry4-18',
//  'twitter-carry4-19',
//  'twitter-carry4-20',
//  'twitter-carry5-1',
//  'twitter-carry5-2',
//  'twitter-carry5-3',
//  'twitter-carry5-4',
//  'twitter-carry5-5',
//  'twitter-carry5-6',
//  'twitter-carry5-7',
//  'twitter-carry5-8',
//  'twitter-carry5-9',
//  'twitter-carry5-10',
//  'twitter-carry5-11',
//  'twitter-carry5-12',
//  'twitter-carry5-13',
//  'twitter-carry5-14',
//  'twitter-carry5-15',
//  'twitter-carry5-16',
//  'twitter-carry5-17',
//  'twitter-carry5-18',
//  'twitter-carry5-19',
//  'twitter-carry5-20',
//  'twitter-carry6-1',
//  'twitter-carry6-2',
//  'twitter-carry6-3',
//  'twitter-carry6-4',
//  'twitter-carry6-5',
//  'twitter-carry6-6',
//  'twitter-carry6-7',
//  'twitter-carry6-8',
//  'twitter-carry6-9',
//  'twitter-carry6-10',
//  'twitter-carry6-11',
//  'twitter-carry6-12',
//  'twitter-carry6-13',
//  'twitter-carry6-14',
//  'twitter-carry6-15',
//  'twitter-carry6-16',
//  'twitter-carry6-17',
//  'twitter-carry6-18',
//  'twitter-carry6-19',
//  'twitter-carry6-20',
//  'twitter-carry7-1',
//  'twitter-carry7-2',
//  'twitter-carry7-3',
//  'twitter-carry7-4',
//  'twitter-carry7-5',
//  'twitter-carry7-6',
//  'twitter-carry7-7',
//  'twitter-carry7-8',
//  'twitter-carry7-9',
//  'twitter-carry7-10',
//  'twitter-carry7-11',
//  'twitter-carry7-12',
//  'twitter-carry7-13',
//  'twitter-carry7-14',
//  'twitter-carry7-15',
//  'twitter-carry7-16',
//  'twitter-carry7-17',
//  'twitter-carry7-18',
//  'twitter-carry7-19',
//  'twitter-carry7-20',
//  'twitter-carry8-1',
//  'twitter-carry8-2',
//  'twitter-carry8-3',
//  'twitter-carry8-4',
//  'twitter-carry8-5',
//  'twitter-carry8-6',
//  'twitter-carry8-7',
//  'twitter-carry8-8',
//  'twitter-carry8-9',
//  'twitter-carry8-10',
//  'twitter-carry8-11',
//  'twitter-carry8-12',
//  'twitter-carry8-13',
//  'twitter-carry8-14',
//  'twitter-carry8-15',
//  'twitter-carry8-16',
//  'twitter-carry8-17',
//  'twitter-carry8-18',
//  'twitter-carry8-19',
//  'twitter-carry8-20',
//  'twitter-carry9-1',
//  'twitter-carry9-2',
//  'twitter-carry9-3',
//  'twitter-carry9-4',
//  'twitter-carry9-5',
//  'twitter-carry9-6',
//  'twitter-carry9-7',
//  'twitter-carry9-8',
//  'twitter-carry9-9',
//  'twitter-carry9-10',
//  'twitter-carry9-11',
//  'twitter-carry9-12',
//  'twitter-carry9-13',
//  'twitter-carry9-14',
//  'twitter-carry9-15',
//  'twitter-carry9-16',
//  'twitter-carry9-17',
//  'twitter-carry9-18',
//  'twitter-carry9-19',
//  'twitter-carry9-20'
// 'twitter-follow-1',
// 'twitter-follow-2',
// 'twitter-follow-3',
// 'twitter-follow-4',
// 'twitter-follow-5',
// 'twitter-follow-6',
// 'twitter-follow-7',
// 'twitter-follow-8',
// 'twitter-follow-9',
// 'twitter-follow-10',
//  'twitter-follow-11',
//  'twitter-follow-12',
//  'twitter-follow-13',
//  'twitter-follow-14',
//  'twitter-follow-15',
// API Key: 76Cd5J6cvfaozPwdpfHTEHfX2

// API Key Secret: tdIk3DzDCaqM0hma3I6PWTXEl3VkDHlWbEnoV0NQ5GIwmGzMqn
    ],
    session_id: "",
    config: {},
    agents: {},
    session_iterator: 0,
    query_iterator: 0,
    follow_iterator: 0,
    login_status: {}
  }),
  sockets: {
    connect: function() {
      //与socket.io连接后回调
      this.$socket.emit("receive", "manager");
      this.$socket.emit("create", "room1");
    },
    ack_init(event) {
      console.log("ack_init");
      console.log("event", event.agents);
      this.query_iterator = 0;
      this.follow_iterator = 0;
      this.agents = event.agents;
      this.profiles = event.profiles_status;
      this.login_status = event.login_status;
    },
    ack_init_agent(agent_id) {
      console.log("ack_init_agent");
      console.log("this agent", this.agents);
      console.log(agent_id);
      console.log(this.agents[agent_id]);
      this.agents[agent_id].init = true;
      let ok = Object.keys(this.agents)
        .map(k => this.agents[k].init)
        .reduce((p, c) => p && c);
      if (ok) this.login();
    },
    screenshot(event) {
      if (this.agents[event.id])
        this.agents[
          event.id
        ].image_data = `data:image/png;base64, ${event.data}`;
      this.$forceUpdate();
    },
    end_query(event) {
      console.log("end query");
      this.config.queries_status[event.agent_id][
        this.query_iterator - 1
      ].status = "ok";

      let ok = Object.keys(this.config.agents)
        .map(agent => {
          if (this.config.queries_status[agent][this.query_iterator - 1]) {
            return this.config.queries_status[agent][this.query_iterator - 1]
              .status;
          }
          return "ok";
        })
        .every(v => v == "ok");

      if (ok) {
        if (
          this.query_iterator ==
          this.config.queries_status[event.agent_id].length
        ) {
          this.next_session();
        } else {
          this.next_query();
        }
      }
      console.log("finish query");
    },
    end_follow(event) {
      let index = this.config.profiles_status[event.agent_id].findIndex(
        p => p.profile == event.profile
      );
      this.config.profiles_status[event.agent_id][index].status = "ok";
      console.log("end follow");
      let ok = Object.keys(this.config.agents)
        .map(agent => {
          if (this.config.profiles_status[agent][this.follow_iterator - 1]) {
            return this.config.profiles_status[agent][this.follow_iterator - 1]
              .status;
          }
          return "ok";
        })
        .every(v => v == "ok");

      console.log(
        this.follow_iterator,
        this.config.profiles_status[event.agent_id].length
      );
      if (ok) {
        if (
          this.follow_iterator ==
          this.config.profiles_status[event.agent_id].length
        ) {
          this.next_query();
        } else {
          this.next_follow();
        }
      }
    },
    ack_login({ agent_id }) {
      this.login_status[agent_id] = true;

      let ok = Object.keys(this.login_status)
        .map(k => this.login_status[k])
        .reduce((p, c) => p && c);

      if (ok) {
        console.log("all agents logined");
        this.run_followings();
      }
    }
  },
  components: {
    StatusIcon
  },
  methods: {
    init() {
      // console.log(this.sessions[this.session_iterator])
      this.config = init_config(this.sessions[this.session_iterator]);
      this.$socket.emit("init", this.config);
    },
    next_session() {
      console.log("finish session");
      this.session_iterator++;
      if (this.session_iterator < this.sessions.length) {
        this.init();
      }
    },
    login() {
      this.$socket.emit("login", {});
    },
    login_agent(agent) {
      this.$socket.emit("login_agent", agent.id);
    },
    follow_agent(agent, profile) {
      this.$socket.emit("run_follow", { agent_id: agent.id, profile });
    },
    init_agent() {
      let agent = { id: 1, platform: "google" };
      this.agents.push(agent);

      this.$socket.emit("init_agent", agent);
    },
    send_command() {
      this.$socket.emit("command", this.term);
    },
    write_json() {
      this.$socket.emit();
    },
    run_queries() {
      this.next_query();
    },
    run_followings() {
      this.next_follow();
    },
    next_query() {

      for (let agent in this.config.agents) {
        if (!this.config.queries_status[agent][this.query_iterator]) continue;

        var wait;
        if (this.query_iterator+1!=this.config.queries_status[agent].length){
          wait='t';
        }else{
          wait='f';
        }
        this.$socket.emit("run_query", {
          agent_id: agent,
          query: this.config.queries_status[agent][this.query_iterator].query,
          session_id: this.config.session_id,
          max_results: this.config.max_results,
          date_intervals: this.config.date_intervals,
          interval: this.config.interval,
          cookie: this.config.agents[agent].cookie,
          wait:wait
        });
        this.config.queries_status[agent][this.query_iterator].status =
          "running";
      }

      this.query_iterator++;
    },
    next_follow() {
      console.log("follow");
      for (let agent in this.config.agents) {
        if (!this.config.profiles_status[agent][this.follow_iterator]) continue;
        console.log("run follow", agent);
        this.$socket.emit("run_follow", {
          agent_id: agent,
          profile: this.config.profiles_status[agent][this.follow_iterator]
            .profile
        });
        this.config.profiles_status[agent][this.follow_iterator].status =
          "running";
      }
      this.follow_iterator++;
      console.log("finish next follow");
    }
  }
};
</script>

<style>
#app {
  font-family: "Avenir", Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
  margin-top: 60px;
}
.screenshot-image {
  border: 1px solid #ccc;
}
</style>

function newFunction() {
  let wait;
  return wait;
}
