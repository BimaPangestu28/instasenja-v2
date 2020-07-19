/* eslint-disable */

<template>
  <div id="app">
    <div
      id="kt_body"
      :style="{backgroundImage: 'url(' + require('@/assets/images/bg.jpg') + ')'}"
      class="quick-panel-right demo-panel-right offcanvas-right header-fixed subheader-enabled page-loading"
    >
      <!--begin::Main-->
      <!--begin::Header Mobile-->
      <div id="kt_header_mobile" class="header-mobile">
        <!--begin::Logo-->
        <a href="/metronic/preview/demo2/index.html">
          <img
            alt="Logo"
            :src="require('@/assets/images/gogarmen.png')"
            class="logo-default max-h-30px"
          />
        </a>
        <!--end::Logo-->

        <!--begin::Toolbar-->
        <div class="d-flex align-items-center">
          <button class="btn p-0 burger-icon burger-icon-left ml-4" id="kt_header_mobile_toggle">
            <span></span>
          </button>

          <button
            class="btn btn-icon btn-hover-transparent-white p-0 ml-3"
            id="kt_header_mobile_topbar_toggle"
          >
            <span class="svg-icon svg-icon-xl">
              <!--begin::Svg Icon | path:/metronic/themes/metronic/theme/html/demo2/dist/assets/media/svg/icons/General/User.svg-->
              <svg
                xmlns="http://www.w3.org/2000/svg"
                xmlns:xlink="http://www.w3.org/1999/xlink"
                width="24px"
                height="24px"
                viewBox="0 0 24 24"
                version="1.1"
              >
                <g stroke="none" stroke-width="1" fill="none" fill-rule="evenodd">
                  <polygon points="0 0 24 0 24 24 0 24" />
                  <path
                    d="M12,11 C9.790861,11 8,9.209139 8,7 C8,4.790861 9.790861,3 12,3 C14.209139,3 16,4.790861 16,7 C16,9.209139 14.209139,11 12,11 Z"
                    fill="#000000"
                    fill-rule="nonzero"
                    opacity="0.3"
                  />
                  <path
                    d="M3.00065168,20.1992055 C3.38825852,15.4265159 7.26191235,13 11.9833413,13 C16.7712164,13 20.7048837,15.2931929 20.9979143,20.2 C21.0095879,20.3954741 20.9979143,21 20.2466999,21 C16.541124,21 11.0347247,21 3.72750223,21 C3.47671215,21 2.97953825,20.45918 3.00065168,20.1992055 Z"
                    fill="#000000"
                    fill-rule="nonzero"
                  />
                </g>
              </svg>
              <!--end::Svg Icon-->
            </span>
          </button>
        </div>
        <!--end::Toolbar-->
      </div>
      <!--end::Header Mobile-->
      <div class="d-flex flex-column flex-root">
        <!--begin::Page-->
        <div class="d-flex flex-row flex-column-fluid page">
          <!--begin::Wrapper-->
          <div class="d-flex flex-column flex-row-fluid wrapper" id="kt_wrapper">
            <!--begin::Header-->
            <div id="kt_header" class="header header-fixed">
              <!--begin::Container-->
              <div class="container d-flex align-items-stretch justify-content-between">
                <!--begin::Left-->
                <div class="d-flex align-items-stretch mr-3">
                  <!--begin::Header Logo-->
                  <div class="header-logo">
                    <a href="/metronic/preview/demo2/index.html">
                      <img
                        alt="Logo"
                        :src="require('@/assets/images/gogarmen.png')"
                        class="logo-default max-h-40px"
                      />
                      <img
                        alt="Logo"
                        :src="require('@/assets/images/gogarmen.png')"
                        class="logo-sticky max-h-40px"
                      />
                    </a>
                  </div>
                  <!--end::Header Logo-->

                  <!--begin::Header Menu Wrapper-->
                  <div
                    class="header-menu-wrapper header-menu-wrapper-left"
                    id="kt_header_menu_wrapper"
                  >
                    <!--begin::Header Menu-->
                    <div
                      id="kt_header_menu"
                      class="header-menu header-menu-left header-menu-mobile header-menu-layout-default"
                    >
                      <!--begin::Header Nav-->
                      <ul class="menu-nav">
                        <li
                          class="menu-item menu-item-submenu menu-item-rel"
                          data-menu-toggle="click"
                          aria-haspopup="true"
                        >
                          <router-link :to="{ name: 'Home' }" class="menu-link menu-toggle">
                            <span class="menu-text">History Log</span>
                          </router-link>
                        </li>
                        <li
                          class="menu-item menu-item-submenu menu-item-rel"
                          data-menu-toggle="click"
                          aria-haspopup="true"
                        >
                          <router-link :to="{ name: 'Account' }" class="menu-link menu-toggle">
                            <span class="menu-text">Account Instagram</span>
                          </router-link>
                        </li>
                        <li
                          class="menu-item menu-item-submenu menu-item-rel"
                          data-menu-toggle="click"
                          aria-haspopup="true"
                        >
                          <router-link :to="{ name: 'BotAccount' }" class="menu-link menu-toggle">
                            <span class="menu-text">Account Bot</span>
                          </router-link>
                        </li>
                        <li
                          class="menu-item menu-item-submenu menu-item-rel"
                          data-menu-toggle="click"
                          aria-haspopup="true"
                        >
                          <router-link :to="{ name: 'FakeComment' }" class="menu-link menu-toggle">
                            <span class="menu-text">Fake Comment</span>
                          </router-link>
                        </li>
                        <li
                          class="menu-item menu-item-submenu menu-item-rel"
                          data-menu-toggle="click"
                          aria-haspopup="true"
                        >
                          <router-link :to="{ name: 'ContactScraping' }" class="menu-link menu-toggle">
                            <span class="menu-text">Contact Scraping</span>
                          </router-link>
                        </li>
                        <li
                          class="menu-item menu-item-submenu menu-item-rel"
                          data-menu-toggle="click"
                          aria-haspopup="true"
                        >
                          <router-link :to="{ name: 'Action' }" class="menu-link menu-toggle">
                            <span class="menu-text">Actions</span>
                          </router-link>
                        </li>
                      </ul>
                      <!--end::Header Nav-->
                    </div>
                    <!--end::Header Menu-->
                  </div>
                  <!--end::Header Menu Wrapper-->
                </div>
                <!--end::Left-->
              </div>
              <!--end::Container-->
            </div>
            <!--end::Header-->

            <!--begin::Content-->
            <div class="content d-flex flex-column flex-column-fluid" id="kt_content">
              <router-view></router-view>
            </div>
            <!--end::Content-->
          </div>
          <!--end::Wrapper-->
        </div>
        <!--end::Page-->
      </div>
      <!--end::Main-->

      <!--begin::Scrolltop-->
      <div id="kt_scrolltop" class="scrolltop">
        <span class="svg-icon">
          <!--begin::Svg Icon | path:/metronic/themes/metronic/theme/html/demo2/dist/assets/media/svg/icons/Navigation/Up-2.svg-->
          <svg
            xmlns="http://www.w3.org/2000/svg"
            xmlns:xlink="http://www.w3.org/1999/xlink"
            width="24px"
            height="24px"
            viewBox="0 0 24 24"
            version="1.1"
          >
            <g stroke="none" stroke-width="1" fill="none" fill-rule="evenodd">
              <polygon points="0 0 24 0 24 24 0 24" />
              <rect fill="#000000" opacity="0.3" x="11" y="10" width="2" height="10" rx="1" />
              <path
                d="M6.70710678,12.7071068 C6.31658249,13.0976311 5.68341751,13.0976311 5.29289322,12.7071068 C4.90236893,12.3165825 4.90236893,11.6834175 5.29289322,11.2928932 L11.2928932,5.29289322 C11.6714722,4.91431428 12.2810586,4.90106866 12.6757246,5.26284586 L18.6757246,10.7628459 C19.0828436,11.1360383 19.1103465,11.7686056 18.7371541,12.1757246 C18.3639617,12.5828436 17.7313944,12.6103465 17.3242754,12.2371541 L12.0300757,7.38413782 L6.70710678,12.7071068 Z"
                fill="#000000"
                fill-rule="nonzero"
              />
            </g>
          </svg>
          <!--end::Svg Icon-->
        </span>
      </div>
      <!--end::Scrolltop-->
    </div>
  </div>
</template>

<style lang="scss">
.router-link-exact-active {
  background-color: rgba(255, 255, 255, 0.1);
}
</style>
