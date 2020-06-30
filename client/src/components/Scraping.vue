<template>
  <!--begin::Entry-->
  <div class="d-flex flex-column-fluid">
    <div class="card card-custom">
      <div class="card-body">
        <div class="tab-content">
          <div class="tab-pane fade active show" v-if="onProcess">
            <button class="btn btn-primary form-control btn-sm mb-12">Reset Action</button>
            <p class="text-center">
              <b>You're action progress still works</b>
            </p>
            <div class="progress mb-12">
              <div
                class="progress-bar progress-bar-striped progress-bar-animated bg-primary"
                role="progressbar"
                :style="`width: 100%`"
                aria-valuenow="100"
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

          <div class="tab-pane fade active show" role="tabpanel" v-if="!onProcess">
            <form class="form">
              <div class="card-body">
                <div class="form-group row">
                  <div class="col-lg-12">
                    <label>Keyword:</label>
                    <input
                      type="text"
                      class="form-control"
                      placeholder="Enter keyword"
                      v-model="data.keyword"
                    />
                    <span class="form-text text-muted">Please enter your keyword</span>
                  </div>
                </div>
              </div>
              <div class="card-footer">
                <div class="row">
                  <div class="col-lg-12">
                    <button
                      type="reset"
                      class="btn btn-primary form-control"
                      @click="process"
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

      notices: [],
      randomCode: Math.floor(Math.random() * 100) + 1,

      data: {
        keyword: ""
      }
    };
  },

  methods: {
    process() {
      this.onProcess = true;

      this.data.random_code = this.randomCode;

      axios
        .post("http://localhost:8001/api/v1/actions/scraping-data", this.data)
        .then(() => {
          this.data = {
            keyword: ""
          };
          this.onProcess = false;
        });
    }
  },

  mounted() {
    var channel = this.$pusher.subscribe("notice");

    channel.bind("log-" + this.randomCode, data => {
      data.datetime = new Date();

      this.notices.push(data);
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