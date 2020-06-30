<template>
  <div>
    <Subheader title="Fake Comment" subtitle="List of fake comment for instagram" />
    <Table
      title="Fake Comment"
      subtitle="You can read all fake comment instagram"
      :payloads="payloads"
      :fields="['comment', 'category']"
      :create="true"
      :showForm.sync="showForm"
      v-if="showForm == false"
      :destroy="destroy"
      :indexEdit.sync="indexEdit"
      :canPrev.sync="canPrev"
      :canNext.sync="canNext"
      :totalPaginate.sync="totalPaginate"
      :paginateSelect.sync="paginateSelect"
    />

    <Form
      title="Fake Comment"
      subtitle="You can create or upate fake comment instagram"
      v-else
      :showForm.sync="showForm"
      :submit="submit"
      :indexEdit.sync="indexEdit"
    >
      <div class="form-group row">
        <div class="col-lg-6">
          <label>Comment:</label>
          <textarea
            type="text"
            class="form-control"
            placeholder="Enter comment"
            v-model="data.comment"
          />
          <span class="form-text text-muted">Please enter your comment</span>
        </div>
        <div class="col-lg-6">
          <label>Category:</label>
          <select
            type="text"
            class="form-control"
            placeholder="Enter category"
            v-model="data.category"
          >
            <option value="promo">Promo</option>
            <option value="info">Info</option>
            <option value="news">News</option>
          </select>
          <span class="form-text text-muted">Please enter your category</span>
        </div>
      </div>
    </Form>
  </div>
</template>

<script>
import Subheader from "../components/Subheader";
import Table from "../components/Table";
import Form from "../components/Form";

import axios from "axios";

export default {
  components: {
    Subheader,
    Table,
    Form
  },

  data() {
    return {
      payloads: [],
      showForm: false,
      indexEdit: -1,
      canPrev: false,
      canNext: false,
      totalPaginate: 0,
      paginateSelect: 1,

      data: {
        comment: "",
        category: ""
      }
    };
  },

  watch: {
    indexEdit(val) {
      if (val > -1) {
        this.data = this.payloads[val];
        this.showForm = true;
      } else {
        this.data = {
          comment: "",
          category: ""
        };
        this.showForm = false;
      }
    },

    paginateSelect(val) {
      axios
        .get(
          "http://localhost:8001/api/v1/fake-comments?limit=25&offset=" + 25 * (val - 1)
        )
        .then(data => {
          this.payloads = data.data.results;

          this.canPrev = data.data.previous;
          this.canNext = data.data.next;
          this.totalPaginate = Math.ceil(data.data.count / 25);
        });
    }
  },

  methods: {
    submit() {
      axios.post("http://localhost:8001/api/v1/fake-comments", this.data).then(data => {
        this.payloads.push(data.data);
        this.showForm = false;
      });
    },

    destroy(index) {
      if (
        confirm(
          "Are you sure delete this fake comment ?"
        )
      ) {
        axios
          .delete(
            "http://localhost:8001/api/v1/fake-comments/" + this.payloads[index].id
          )
          .then(() => {
            this.payloads.splice(index, 1);

            alert("Delete fake comment success");
          });
      }
    }
  },

  mounted() {
    axios.get("http://localhost:8001/api/v1/fake-comments?limit=25").then(data => {
      this.payloads = data.data.results;

      this.canPrev = data.data.previous;
      this.canNext = data.data.next;
      this.totalPaginate = Math.ceil(data.data.count / 25);
    });
  }
};
</script>