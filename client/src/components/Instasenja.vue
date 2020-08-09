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
                :class="{'nav-link': true, 'active': tabSelect == 'follow from post'}"
                @click="tabSelect = 'follow from post'"
              >
                <span class="nav-text">Follow From Post</span>
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
            <li class="nav-item">
              <a
                :class="{'nav-link': true, 'active': tabSelect == 'multiple post'}"
                @click="tabSelect = 'multiple post'"
              >
                <span class="nav-text">Multiple Post</span>
              </a>
            </li>
            <li class="nav-item">
              <a
                :class="{'nav-link': true, 'active': tabSelect == 'like by tag'}"
                @click="tabSelect = 'like by tag'"
              >
                <span class="nav-text">Like by hastag</span>
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

          <!-- Start :: Follow From Post -->
          <div
            :class="{'tab-pane': true, 'fade': true, 'active': tabSelect == 'follow from post', 'show': tabSelect == 'follow from post'}"
            role="tabpanel"
            v-if="!onProcess"
          >
            <form class="form">
              <div class="card-body">
                <div class="form-group row">
                  <div class="col-lg-6">
                    <label>Account:</label>
                    <select
                      type="text"
                      class="form-control"
                      placeholder="Select account"
                      v-model="data.account_id"
                    >
                      <option
                        :value="account.id"
                        v-for="account in accounts"
                        :key="account.username"
                      >{{ account.username }}</option>
                    </select>
                    <span class="form-text text-muted">Please select your account</span>
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
              </div>
              <div class="card-footer">
                <div class="row">
                  <div class="col-lg-12">
                    <button
                      type="reset"
                      class="btn btn-primary form-control"
                      @click="process('follow from post')"
                    >Proses</button>
                  </div>
                </div>
              </div>
            </form>
          </div>
          <!-- End :: Follow From Post -->

          <!-- Start :: Like By Hastag -->
          <div
            :class="{'tab-pane': true, 'fade': true, 'active': tabSelect == 'like by tag', 'show': tabSelect == 'like by tag'}"
            role="tabpanel"
            v-if="!onProcess"
          >
            <form class="form">
              <div class="card-body">
                <div class="form-group row">
                  <div class="col-lg-4">
                    <label>Account:</label>
                    <select
                      type="text"
                      class="form-control"
                      placeholder="Select account"
                      v-model="data.account_id"
                    >
                      <option
                        :value="account.id"
                        v-for="account in accounts"
                        :key="account.username"
                      >{{ account.username }}</option>
                    </select>
                    <span class="form-text text-muted">Please select your account</span>
                  </div>
                  <div class="col-lg-4">
                    <label>Total Like:</label>
                    <input
                      type="number"
                      class="form-control"
                      placeholder="Enter url instagram bot"
                      v-model="data.total_like"
                    />
                    <span class="form-text text-muted">Please enter your total like</span>
                  </div>
                  <div class="col-lg-4">
                    <label>Hastag:</label>
                    <input
                      type="text"
                      class="form-control"
                      placeholder="Enter hastah"
                      v-model="data.tag"
                    />
                    <span class="form-text text-muted">Please enter your hastag</span>
                  </div>
                </div>
              </div>
              <div class="card-footer">
                <div class="row">
                  <div class="col-lg-12">
                    <button
                      type="reset"
                      class="btn btn-primary form-control"
                      @click="process('like by tag')"
                    >Proses</button>
                  </div>
                </div>
              </div>
            </form>
          </div>
          <!-- End :: Like By Hastag -->

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
                  <div class="col-lg-4">
                    <label>Account:</label>
                    <select
                      type="text"
                      class="form-control"
                      placeholder="Select account"
                      v-model="data.account_id"
                    >
                      <option
                        :value="account.id"
                        v-for="account in accounts"
                        :key="account.username"
                      >{{ account.username }}</option>
                    </select>
                    <span class="form-text text-muted">Please select your account</span>
                  </div>
                  <div class="col-lg-4">
                    <label>Username Competitor:</label>
                    <input
                      type="text"
                      class="form-control"
                      placeholder="Enter username competitor"
                      v-model="data.username_competitor"
                    />
                    <span class="form-text text-muted">Please enter your username competitor</span>
                  </div>
                  <div class="col-lg-4">
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
                  <div class="col-lg-6">
                    <label>Account:</label>
                    <select
                      type="text"
                      class="form-control"
                      placeholder="Select account"
                      v-model="data.account_id"
                    >
                      <option
                        :value="account.id"
                        v-for="account in accounts"
                        :key="account.username"
                      >{{ account.username }}</option>
                    </select>
                    <span class="form-text text-muted">Please select your account</span>
                  </div>
                  <div class="col-lg-6">
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
          <div
            :class="{'tab-pane': true, 'fade': true, 'active': tabSelect == 'multiple post', 'show': tabSelect == 'multiple post'}"
            role="tabpanel"
            v-if="!onProcess"
          >
            <form class="form">
              <div class="card-body">
                <div class="form-group row">
                  <div class="col-lg-6">
                    <label>Title:</label>
                    <input
                      type="text"
                      class="form-control"
                      placeholder="Enter title"
                      v-model="data.title"
                    />
                    <span class="form-text text-muted">Please enter your title</span>
                  </div>
                  <div class="col-lg-6">
                    <label>Image:</label>
                    <input
                      type="text"
                      class="form-control"
                      placeholder="Enter image"
                      v-model="data.image"
                    />
                    <span class="form-text text-muted">Please enter your image</span>
                  </div>
                </div>
                <div class="form-group row">
                  <div class="col-lg-12">
                    <label>Description:</label>
                    <textarea
                      type="text"
                      class="form-control"
                      placeholder="Enter description"
                      v-model="data.description"
                    />
                    <span class="form-text text-muted">Please enter your description</span>
                  </div>
                </div>
                <div class="form-group row">
                  <div class="col-lg-12">
                    <table
                      class="table table-separate table-head-custom table-checkable"
                      id="kt_datatable_2"
                    >
                      <thead>
                        <tr>
                          <th>#</th>
                          <th>Username</th>
                          <th>Password</th>
                          <th>Actions</th>
                        </tr>
                      </thead>

                      <tbody>
                        <tr v-for="(account, index) in data.accounts" :key="`account-${index}`">
                          <td>{{ index += 1 }}</td>
                          <td>
                            <input
                              type="text"
                              class="form-control"
                              placeholder="Enter username"
                              v-model="account.username"
                            />
                          </td>
                          <td>
                            <input
                              type="text"
                              class="form-control"
                              placeholder="Enter password"
                              v-model="account.password"
                            />
                          </td>
                          <td>
                            <button
                              class="btn btn-danger font-weight-bolder ml-5"
                              @click="removeAccount(index-1)"
                            >
                              <span class="svg-icon svg-icon-default">
                                <!--begin::Svg Icon | path:/home/keenthemes/www/metronic/themes/metronic/theme/html/demo2/dist/../src/media/svg/icons/Home/Trash.svg-->
                                <svg
                                  xmlns="http://www.w3.org/2000/svg"
                                  xmlns:xlink="http://www.w3.org/1999/xlink"
                                  width="24px"
                                  height="24px"
                                  viewBox="0 0 24 24"
                                  version="1.1"
                                >
                                  <g
                                    stroke="none"
                                    stroke-width="1"
                                    fill="none"
                                    fill-rule="evenodd"
                                  >
                                    <rect x="0" y="0" width="24" height="24" />
                                    <path
                                      d="M6,8 L18,8 L17.106535,19.6150447 C17.04642,20.3965405 16.3947578,21 15.6109533,21 L8.38904671,21 C7.60524225,21 6.95358004,20.3965405 6.89346498,19.6150447 L6,8 Z M8,10 L8.45438229,14.0894406 L15.5517885,14.0339036 L16,10 L8,10 Z"
                                      fill="#000000"
                                      fill-rule="nonzero"
                                    />
                                    <path
                                      d="M14,4.5 L14,3.5 C14,3.22385763 13.7761424,3 13.5,3 L10.5,3 C10.2238576,3 10,3.22385763 10,3.5 L10,4.5 L5.5,4.5 C5.22385763,4.5 5,4.72385763 5,5 L5,5.5 C5,5.77614237 5.22385763,6 5.5,6 L18.5,6 C18.7761424,6 19,5.77614237 19,5.5 L19,5 C19,4.72385763 18.7761424,4.5 18.5,4.5 L14,4.5 Z"
                                      fill="#000000"
                                      opacity="0.3"
                                    />
                                  </g>
                                </svg>
                                <!--end::Svg Icon-->
                              </span> Hapus
                            </button>
                          </td>
                        </tr>
                        <tr>
                          <td colspan="4">
                            <button
                              class="btn btn-primary form-control"
                              @click="addAccount"
                            >Add New Account</button>
                          </td>
                        </tr>
                      </tbody>
                    </table>
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
      accounts: [],

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
        total_follow: 0,
        account_id: "",
        tag: "",
        accounts: [
          {
            username: "",
            password: ""
          }
        ]
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
    addAccount() {
      this.data.accounts.push({ username: "", password: "" });
    },

    removeAccount(index) {
      this.data.accounts.splice(index, 1);
    },

    process(type) {
      this.percentage = 0;
      this.totalProcess = 0;
      this.onProcess = true;
      this.notices = [];

      this.data.random_code = this.randomCode;

      let url = "";

      switch (type) {
        case "like & comment":
          url = "http://localhost:8001/api/v1/actions/like-comment-post";
          break;

        case "unfollow":
          url = "http://localhost:8001/api/v1/actions/unfollow";
          break;

        case "get user from competitor":
          url = "http://localhost:8001/api/v1/actions/follow-from-competitor";
          break;

        case "follow from post":
          url = "http://localhost:8001/api/v1/actions/follow-from-post";
          break;

        case "like by tag":
          url = "http://localhost:8001/api/v1/actions/like-by-tag";
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
          total_follow: 0,
          account_id: "",
          tag: ""
        };
      });
    }
  },

  mounted() {
    var channel = this.$pusher.subscribe("notice");

    axios.get("http://localhost:8001/api/v1/accounts?limit=999").then(data => {
      this.accounts = data.data.results;
    });

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