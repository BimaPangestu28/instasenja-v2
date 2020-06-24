<template>
  <div>
    <Subheader title="Action" subtitle="All actions for we business" />

    <!--begin::Entry-->
    <div class="d-flex flex-column-fluid">
      <!--begin::Container-->
      <div class="container">
        <div class="card card-custom">
          <div class="card-header card-header-tabs-line">
            <div class="card-toolbar">
              <ul class="nav nav-tabs nav-bold nav-tabs-line">
                <li class="nav-item">
                  <a
                    :class="{'nav-link': true, 'active': selectTab == 'scraping data'}"
                    data-toggle="tab"
                    href="#kt_tab_pane_1_4"
                    @click="selectTab = 'scraping data'"
                  >
                    <span class="nav-text">Scraping Data</span>
                  </a>
                </li>
                <li class="nav-item">
                  <a
                    :class="{'nav-link': true, 'active': selectTab == 'instasenja'}"
                    data-toggle="tab"
                    href="#kt_tab_pane_2_4"
                    @click="selectTab = 'instasenja'"
                  >
                    <span class="nav-text">Instasenja</span>
                  </a>
                </li>
              </ul>
            </div>
          </div>
          <div class="card-body">
            <div class="tab-content">
              <div
                :class="{'tab-pane': true, 'fade': true, 'active': selectTab == 'scraping data','show': selectTab == 'scraping data'}"
                id="kt_tab_pane_1_4"
                role="tabpanel"
                aria-labelledby="kt_tab_pane_1_4"
                v-if="selectTab == 'scraping data'"
              >
                <Scraping/>
              </div>
              <div
                :class="{'tab-pane': true, 'fade': true, 'active': selectTab == 'instasenja','show': selectTab == 'instasenja'}"
                id="kt_tab_pane_2_4"
                role="tabpanel"
                aria-labelledby="kt_tab_pane_2_4"
                v-else-if="selectTab == 'instasenja'"
              >
                <Instasenja/>
              </div>
            </div>
          </div>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
import Subheader from "../components/Subheader";
import Instasenja from "../components/Instasenja";
import Scraping from "../components/Scraping";

export default {
  components: {
    Subheader,
    Instasenja,
    Scraping,
  },

  data() {
    return {
      selectTab: "scraping data"
    };
  }
};
</script>