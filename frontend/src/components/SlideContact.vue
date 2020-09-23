<template>
  <section class="cv-details-section contact">
    <div class="page-title">
      <h2>Contact</h2>
    </div>

    <div class="cv-details-section-content">

      <div class="row">
        <div class="cv-details-section-content-left">
          <div class="lm-info-block gray-default">
            <font-awesome-icon icon="map-marker-alt"/>
            <h4>Belarus, Minsk</h4>
            <span class="lm-info-block-value"></span>
            <span class="lm-info-block-text"></span>
          </div>

          <div class="lm-info-block gray-default">
            <a href="mailto:sergey.bondar.dev@gmail.com">
              <font-awesome-icon icon="envelope"/>
              <h4>
                sergey.bondar.dev@gmail.com
              </h4>
            </a>
            <span class="lm-info-block-value"></span>
            <span class="lm-info-block-text"></span>
          </div>

          <div class="lm-info-block gray-default">
            <a href="https://telegram.me/sbondar_tg">
              <font-awesome-icon icon="paper-plane"/>
              <h4>
                sbondar_tg
              </h4>
            </a>
            <span class="lm-info-block-value"></span>
            <span class="lm-info-block-text"></span>
          </div>

        </div>

        <div class="cv-details-section-content-right">
          <div class="block-title">
            <h3>How Can I Help You?</h3>
          </div>

          <form id="contact_form" class="contact-form" action="" method="post"
                novalidate="true" @submit="checkForm">

            <div class="messages"></div>

            <div class="controls two-columns">
              <div class="fields clearfix">
                <div class="left-column">
                  <div class="form-group form-group-with-icon"
                       :class="{ 'form-group-focus': form.fullName.value, 'has-error': form.fullName.hasError}">
                    <input type="text" class="form-control"
                           v-model="form.fullName.value" @change="checkField(form.fullName)">
                    <label>Full Name</label>
                    <div class="form-control-border"></div>
                    <div class="help-block with-errors" v-if="form.fullName.errors.length">
                      <span v-for="error in form.fullName.errors" :key="error">{{ error }}</span>
                    </div>
                  </div>

                  <div class="form-group form-group-with-icon"
                       :class="{ 'form-group-focus': form.email.value, 'has-error': form.email.hasError}">
                    <input type="email" class="form-control"
                           v-model="form.email.value" @change="checkField(form.email)">
                    <label>Email Address</label>
                    <div class="help-block with-errors" v-if="form.email.errors.length">
                      <span v-for="error in form.email.errors" :key="error">{{ error }}</span>
                    </div>
                  </div>

                  <div class="form-group form-group-with-icon"
                       :class="{ 'form-group-focus': form.subject.value, 'has-error': form.subject.hasError}">
                    <input type="text" class="form-control"
                           v-model="form.subject.value" @change="checkField(form.subject)">
                    <label>Subject</label>
                    <div class="help-block with-errors" v-if="form.subject.errors.length">
                      <span v-for="error in form.subject.errors" :key="error">{{ error }}</span>
                    </div>
                  </div>
                </div>
                <div class="right-column">
                  <div class="form-group form-group-with-icon"
                       :class="{ 'form-group-focus': form.message.value, 'has-error': form.message.hasError}">
                    <textarea class="form-control" rows="7"
                              v-model="form.message.value" @change="checkField(form.message)">>
                    </textarea>
                    <label>Message</label>
                    <div class="help-block with-errors" v-if="form.message.errors.length">
                      <span v-for="error in form.message.errors" :key="error">{{ error }}</span>
                    </div>
                  </div>
                </div>
              </div>

              <div class="g-recaptcha" data-sitekey="6LdqmCAUAAAAAMMNEZvn6g4W5e0or2sZmAVpxVqI">
                <div style="width: 304px; height: 78px;">
                  <div>
                    <iframe
                      src="https://www.google.com/recaptcha/api2/anchor?ar=1&amp;k=6LdqmCAUAAAAAMMNEZvn6g4W5e0or2sZmAVpxVqI&amp;co=aHR0cHM6Ly9sbXBpeGVscy5jb206NDQz&amp;hl=en&amp;v=6TWYOsKNtRFaLeFqv5xN42-l&amp;size=normal&amp;cb=fyv45cyj3z7c"
                      width="304" height="78" role="presentation" name="a-fqarljb6vcbq" frameborder="0" scrolling="no"
                      sandbox="allow-forms allow-popups allow-same-origin allow-scripts allow-top-navigation allow-modals allow-popups-to-escape-sandbox"></iframe>
                  </div>
                  <textarea id="g-recaptcha-response" name="g-recaptcha-response" class="g-recaptcha-response"
                            style="width: 250px; height: 40px; border: 1px solid rgb(193, 193, 193); margin: 10px 25px; padding: 0px; resize: none; display: none;"></textarea>
                </div>
                <iframe style="display: none;"></iframe>
              </div>

              <input type="submit" class="button btn-send disabled" value="Send message">
            </div>
          </form>
        </div>
      </div>

    </div>
  </section>
</template>

<script>

  export default {
    name: "Contact",
    data() {
      return {
        form: {
          fullName: {
            name: 'Full Name',
            value: '',
            hasError: false,
            type: 'text',
            errors: []
          },
          email: {
            name: 'Email Address',
            value: '',
            hasError: false,
            type: 'email',
            errors: []
          },
          subject: {
            name: 'Subject',
            value: '',
            hasError: false,
            type: 'text',
            errors: []
          },
          message: {
            name: 'Message',
            value: '',
            hasError: false,
            type: 'text',
            errors: []
          }
        }
      }
    },
    methods: {
      emailIsValid: function (email) {
        const re = /^(([^<>()[\]\\.,;:\s@"]+(\.[^<>()[\]\\.,;:\s@"]+)*)|(".+"))@((\[[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\])|(([a-zA-Z\-0-9]+\.)+[a-zA-Z]{2,}))$/;
        return re.test(email);
      },
      checkField(field) {
        field.errors = []
        if (field.value === '') {
          field.errors.push(`${field.name} is required.`)
        } else if (field.type === 'email' && !this.emailIsValid(field.value)) {
          field.errors.push(`${field.name} is not valid.`)
        }

        if (field.errors.length) {
          field.hasError = true;
        }
      },
      checkForm(e) {
        e.preventDefault()
        for (let key in this.form) {
          this.checkField(this.form[key])
        }
      }
    }
  }
</script>

<style scoped>

</style>
