<template>
  <!--begin::Entry-->
  <div class="d-flex flex-column-fluid">
    <!--begin::Container-->
    <div class="container">
      <!--begin::Card-->
      <div class="card card-custom gutter-b example example-compact">
        <div class="card-header">
          <div class="card-title">
            <h3 class="card-label">
              {{ title }}
              <span class="d-block text-muted pt-2 font-size-sm">{{ subtitle }}</span>
            </h3>
          </div>
          <div class="card-toolbar">
            <a
              href="#"
              class="btn btn-danger font-weight-bolder mr-5"
              @click="$emit('update:showForm', false); $emit('update:indexEdit', -1)"
            >Cancel</a>

            <a href="#" class="btn btn-primary font-weight-bolder" @click="submit">Submit</a>
          </div>
        </div>
        <!--begin::Form-->
        <form class="form">
          <div class="card-body">
            <slot></slot>
          </div>
        </form>
        <!--end::Form-->
      </div>
    </div>
  </div>
</template>

<script>
export default {
  props: ["title", "subtitle", "showForm", "submit", "indexEdit"]
};
</script>