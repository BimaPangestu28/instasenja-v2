<template>
  <!--begin::Entry-->
  <div class="d-flex flex-column-fluid">
    <div class="card card-custom">
      <div class="card-header card-header-tabs-line">
        <div class="card-toolbar">
          <ul class="nav nav-tabs nav-bold nav-tabs-line">
            <li class="nav-item">
              <a
                :class="{'nav-link': true, 'active': tabSelect == 'auto like & comment'}"
                @click="tabSelect = 'auto like & comment'"
              >
                <span class="nav-text">Auto Like & Comment</span>
              </a>
            </li>
            <li class="nav-item">
              <a
                :class="{'nav-link': true, 'active': tabSelect == 'get user from competitor'}"
                @click="tabSelect = 'get user from competitor'"
              >
                <span class="nav-text">Follow From Competitor</span>
              </a>
            </li>
            <li class="nav-item">
              <a
                :class="{'nav-link': true, 'active': tabSelect == 'unfollow'}"
                @click="tabSelect = 'unfollow'"
              >
                <span class="nav-text">Unfollow</span>
              </a>
            </li>
          </ul>
        </div>
      </div>
      <div class="card-body">
        <div class="tab-content">
          <div class="tab-pane fade active show" v-if="onProcess">
            <button
              class="btn btn-primary form-control btn-sm mb-12"
              v-if="percentage == 100"
              @click="onProcess = false"
            >Reset Action</button>
            <p class="text-center">
              <b>You're action progress on {{percentage}}%</b>
            </p>
            <div class="progress mb-12">
              <div
                class="progress-bar progress-bar-striped progress-bar-animated bg-primary"
                role="progressbar"
                :style="`width: ${percentage}%`"
                :aria-valuenow="percentage"
                aria-valuemin="0"
                aria-valuemax="100"
              ></div>
            </div>
            <p class="text-center">
              <b>Log history for your action :</b>
            </p>
            <!--begin: Datatable-->
            <table
              class="table table-separate table-head-custom table-checkable"
              id="kt_datatable_2"
            >
              <thead>
                <tr>
                  <th>#</th>
                  <th>Description</th>
                  <th>State</th>
                  <th>Datetime</th>
                </tr>
              </thead>

              <tbody v-if="notices.length > 0">
                <tr v-for="(notice, index) in notices" :key="`notice-${index}`">
                  <td>{{ index += 1 }}</td>
                  <td>{{ notice.message }}</td>
                  <td>{{ notice.type }}</td>
                  <td>{{ notice.datetime }}</td>
                </tr>
              </tbody>
              <tbody v-else>
                <tr>
                  <td colspan="4" class="text-center">
                    <p>Nothing notices for now</p>
                  </td>
                </tr>
              </tbody>
            </table>
          </div>

          <div
            :class="{'tab-pane': true, 'fade': true, 'active': tabSelect == 'auto like & comment', 'show': tabSelect == 'auto like & comment'}"
            role="tabpanel"
            v-if="!onProcess"
          >
            <form class="form">
              <div class="card-body">
                <div class="form-group row">
                  <div class="col-lg-6">
                    <label>Comment Category:</label>
                    <select
                      type="text"
                      class="form-control"
                      placeholder="Select comment category"
                      v-model="data.comment_category"
                    >
                      <option value="promo">Promo</option>
                      <option value="info">Info</option>
                      <option value="news">News</option>
                    </select>
                    <span class="form-text text-muted">Please select your comment category</span>
                  </div>
                  <div class="col-lg-6">
                    <label>URL Instagram Post:</label>
                    <input
                      type="text"
                      class="form-control"
                      placeholder="Enter url instagram bot"
                      v-model="data.url"
                    />
                    <span class="form-text text-muted">Please enter your url instagram bot</span>
                  </div>
                </div>
                <div class="form-group row">
                  <div class="col-lg-6">
                    <label>Total Like:</label>
                    <input
                      type="text"
                      class="form-control"
                      placeholder="Enter total like"
                      v-model="data.total_like"
                    />
                    <span class="form-text text-muted">Please enter your total like</span>
                  </div>
                  <div class="col-lg-6">
                    <label>Total Comment:</label>
                    <input
                      type="text"
                      class="form-control"
                      placeholder="Enter total comment"
                      v-model="data.total_comment"
                    />
                    <span class="form-text text-muted">Please enter your total comment</span>
                  </div>
                </div>
              </div>
              <div class="card-footer">
                <div class="row">
                  <div class="col-lg-12">
                    <button
                      type="reset"
                      class="btn btn-primary form-control"
                      @click="process('like & comment')"
                    >Proses</button>
                  </div>
                </div>
              </div>
            </form>
          </div>
          <div
            :class="{'tab-pane': true, 'fade': true, 'active': tabSelect == 'get user from competitor', 'show': tabSelect == 'get user from competitor'}"
            v-if="!onProcess"
          >
            <form class="form">
              <div class="card-body">
                <div class="form-group row">
                  <div class="col-lg-6">
                    <label>Username:</label>
                    <input
                      type="text"
                      class="form-control"
                      placeholder="Enter username"
                      v-model="data.username"
                    />
                    <span class="form-text text-muted">Please enter your username</span>
                  </div>
                  <div class="col-lg-6">
                    <label>Password:</label>
                    <input
                      type="text"
                      class="form-control"
                      placeholder="Enter password"
                      v-model="data.password"
                    />
                    <span class="form-text text-muted">Please enter your password</span>
                  </div>
                </div>
                <div class="form-group row">
                  <div class="col-lg-6">
                    <label>Username Competitor:</label>
                    <input
                      type="text"
                      class="form-control"
                      placeholder="Enter username competitor"
                      v-model="data.username_competitor"
                    />
                    <span class="form-text text-muted">Please enter your username competitor</span>
                  </div>
                  <div class="col-lg-6">
                    <label>Total Folow:</label>
                    <input
                      type="text"
                      class="form-control"
                      placeholder="Enter total follow"
                      v-model="data.total_follow"
                    />
                    <span class="form-text text-muted">Please enter your total follow</span>
                  </div>
                </div>
              </div>
              <div class="card-footer">
                <div class="row">
                  <div class="col-lg-12">
                    <button
                      type="reset"
                      class="btn btn-primary form-control"
                      @click="process('get user from competitor')"
                    >Proses</button>
                  </div>
                </div>
              </div>
            </form>
          </div>
          <div
            :class="{'tab-pane': true, 'fade': true, 'active': tabSelect == 'unfollow', 'show': tabSelect == 'unfollow'}"
            role="tabpanel"
            v-if="!onProcess"
          >
            <form class="form">
              <div class="card-body">
                <div class="form-group row">
                  <div class="col-lg-4">
                    <label>Username:</label>
                    <input
                      type="text"
                      class="form-control"
                      placeholder="Enter username"
                      v-model="data.username"
                    />
                    <span class="form-text text-muted">Please enter your username</span>
                  </div>
                  <div class="col-lg-4">
                    <label>Password:</label>
                    <input
                      type="text"
                      class="form-control"
                      placeholder="Enter password"
                      v-model="data.password"
                    />
                    <span class="form-text text-muted">Please enter your password</span>
                  </div>
                  <div class="col-lg-4">
                    <label>Total unfollow:</label>
                    <input
                      type="text"
                      class="form-control"
                      placeholder="Enter total unfollow"
                      v-model="data.total_unfollow"
                    />
                    <span class="form-text text-muted">Please enter your total unfollow</span>
                  </div>
                </div>
              </div>
              <div class="card-footer">
                <div class="row">
                  <div class="col-lg-12">
                    <button
                      type="reset"
                      class="btn btn-primary form-control"
                      @click="process('unfollow')"
                    >Proses</button>
                  </div>
                </div>
              </div>
            </form>
          </div>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
import axios from "axios";

export default {
  data() {
    return {
      tabSelect: "auto like & comment",
      onProcess: false,
      percentage: 0,
      totalProcess: 0,

      notices: [],
      randomCode: Math.floor(Math.random() * 100) + 1,

      data: {
        total_comment: 0,
        total_like: 0,
        url: "",
        comment_category: "",
        username: "",
        password: "",
        total_unfollow: 0,
        username_competitor: "",
        total_follow: 0
      }
    };
  },

  watch: {
    tabSelect() {
      this.totalProcess = 0;
      this.onProcess = 0;
      this.percentage = 0;
    }
  },

  methods: {
    process(type) {
      this.percentage = 0;
      this.totalProcess = 0;
      this.onProcess = true;

      this.data.random_code = this.randomCode;

      let url = "";

      switch (type) {
        case "like & comment":
          url = "http://localhost:8000/api/v1/actions/like-comment-post";
          break;

        case "unfollow":
          url = "http://localhost:8000/api/v1/actions/unfollow";
          break;

        case "get user from competitor":
          url = "http://localhost:8000/api/v1/actions/follow-from-competitor";
          break;

        default:
          break;
      }

      axios.post(url, this.data).then(() => {
        this.percentage = 100;
        this.data = {
          total_comment: 0,
          total_like: 0,
          url: "",
          comment_category: "",
          username: "",
          password: "",
          total_unfollow: 0,
          username_competitor: "",
          total_follow: 0
        };
      });
    }
  },

  mounted() {
    var channel = this.$pusher.subscribe("notice");

    channel.bind("log-" + this.randomCode, data => {
      data.datetime = new Date();

      this.notices.push(data);

      let original_number = 0;
      switch (this.tabSelect) {
        case "auto like & comment":
          original_number = this.data.total_comment + this.data.total_like;
          break;

        case "unfollow":
          original_number = this.data.total_unfollow;
          break;

        case "get user from competitor":
          original_number = this.data.total_follow;
          break;

        default:
          break;
      }

      this.totalProcess++;
      this.percentage = (this.totalProcess / original_number) * 100;
    });
  }
};
</script>

<style lang="css">
.nav-link {
  cursor: pointer;
}

.card-custom {
  width: 100%;
}
</style>