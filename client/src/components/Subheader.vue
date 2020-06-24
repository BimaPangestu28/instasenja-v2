<template>
<!--begin::Subheader-->
<div class="subheader py-2 py-lg-12 subheader-transparent" id="kt_subheader">
    <div
        class="container d-flex align-items-center justify-content-between flex-wrap flex-sm-nowrap"
    >
        <!--begin::Info-->
        <div class="d-flex align-items-center flex-wrap mr-1">
        <!--begin::Heading-->
        <div class="d-flex flex-column">
            <!--begin::Title-->
            <h2 class="text-white font-weight-bold my-2 mr-5">{{title}}</h2>
            <!--end::Title-->

            <!--begin::Breadcrumb-->
            <div class="d-flex align-items-center font-weight-bold my-2">
            <a
                href
                class="text-white text-hover-white opacity-75 hover-opacity-100"
            >{{subtitle}}</a>
            <!--end::Item-->
            </div>
            <!--end::Breadcrumb-->
        </div>
        <!--end::Heading-->
        </div>
        <!--end::Info-->
    </div>
</div>
<!--end::Subheader-->
</template>

<script>
export default {
    props: ["title", "subtitle"]
}
</script>