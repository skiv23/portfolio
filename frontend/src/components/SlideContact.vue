<template>
  <section class="cv-details-section contact">
    <div class="page-title">
      <h2>Contact</h2>
    </div>

    <div class="cv-details-section-content">

      <div class="row">
        <div class="cv-details-section-content-left">
          <div class="lm-info-block gray-default" v-for="contact in contacts" :key="contact.id">
            <font-awesome-icon :icon="JSON.parse(contact.icon)"/>
            <a v-if="contact.url" :href="contact.url">
              <h4>{{ contact.text }}</h4>
            </a>
            <h4 v-else>{{ contact.text }}</h4>
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
                       :class="{ 'form-group-focus': form.fields.full_name.value, 'has-error': form.fields.full_name.hasError}">
                    <input type="text" class="form-control"
                           v-model="form.fields.full_name.value" @change="checkField(form.fields.full_name)">
                    <label>Full Name</label>
                    <div class="form-control-border"></div>
                    <div class="help-block with-errors" v-if="form.fields.full_name.errors.length">
                      <span v-for="error in form.fields.full_name.errors" :key="error">{{ error }}</span>
                    </div>
                  </div>

                  <div class="form-group form-group-with-icon"
                       :class="{ 'form-group-focus': form.fields.email.value, 'has-error': form.fields.email.hasError}">
                    <input type="email" class="form-control"
                           v-model="form.fields.email.value" @change="checkField(form.fields.email)">
                    <label>Email Address</label>
                    <div class="help-block with-errors" v-if="form.fields.email.errors.length">
                      <span v-for="error in form.fields.email.errors" :key="error">{{ error }}</span>
                    </div>
                  </div>

                  <div class="form-group form-group-with-icon"
                       :class="{ 'form-group-focus': form.fields.subject.value, 'has-error': form.fields.subject.hasError}">
                    <input type="text" class="form-control"
                           v-model="form.fields.subject.value" @change="checkField(form.fields.subject)">
                    <label>Subject</label>
                    <div class="help-block with-errors" v-if="form.fields.subject.errors.length">
                      <span v-for="error in form.fields.subject.errors" :key="error">{{ error }}</span>
                    </div>
                  </div>
                </div>
                <div class="right-column">
                  <div class="form-group form-group-with-icon"
                       :class="{ 'form-group-focus': form.fields.message.value, 'has-error': form.fields.message.hasError}">
                    <textarea class="form-control" rows="7"
                              v-model="form.fields.message.value" @change="checkField(form.fields.message)">>
                    </textarea>
                    <label>Message</label>
                    <div class="help-block with-errors" v-if="form.fields.message.errors.length">
                      <span v-for="error in form.fields.message.errors" :key="error">{{ error }}</span>
                    </div>
                  </div>
                </div>
              </div>

<!--              <div class="g-recaptcha" data-sitekey="6LdqmCAUAAAAAMMNEZvn6g4W5e0or2sZmAVpxVqI">-->
<!--                <div style="width: 304px; height: 78px;">-->
<!--                  <div>-->
<!--                    <iframe-->
<!--                      src="https://www.google.com/recaptcha/api2/anchor?ar=1&amp;k=6LdqmCAUAAAAAMMNEZvn6g4W5e0or2sZmAVpxVqI&amp;co=aHR0cHM6Ly9sbXBpeGVscy5jb206NDQz&amp;hl=en&amp;v=6TWYOsKNtRFaLeFqv5xN42-l&amp;size=normal&amp;cb=fyv45cyj3z7c"-->
<!--                      width="304" height="78" role="presentation" name="a-fqarljb6vcbq" frameborder="0" scrolling="no"-->
<!--                      sandbox="allow-forms allow-popups allow-same-origin allow-scripts allow-top-navigation allow-modals allow-popups-to-escape-sandbox"></iframe>-->
<!--                  </div>-->
<!--                  <textarea id="g-recaptcha-response" name="g-recaptcha-response" class="g-recaptcha-response"-->
<!--                            style="width: 250px; height: 40px; border: 1px solid rgb(193, 193, 193); margin: 10px 25px; padding: 0px; resize: none; display: none;"></textarea>-->
<!--                </div>-->
<!--                <iframe style="display: none;"></iframe>-->
<!--              </div>-->

              <input type="submit" class="button btn-send disabled" value="Send message">
            </div>
          </form>
        </div>
      </div>

    </div>
  </section>
</template>

<script>
  import ContactDataService from '../services/ContactDataService'

  export default {
    name: "Contact",
    data() {
      return {
        contacts: [],
        form: {}
      }
    },
    created() {
      this.resetForm();
    },
    mounted() {
      ContactDataService.filterByComponent('contact')
        .then(response => {
          this.contacts = response.data;
        });
    },
    methods: {
      resetForm() {
        this.form = {
          fields: {
            full_name: {
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
            },
          },
          hasErrors: false,
          data: {}
        }
      },
      emailIsValid: function (email) {
        const re = /^(([^<>()[\]\\.,;:\s@"]+(\.[^<>()[\]\\.,;:\s@"]+)*)|(".+"))@((\[[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\])|(([a-zA-Z\-0-9]+\.)+[a-zA-Z]{2,}))$/;
        return re.test(email);
      },
      checkField(field, fieldName) {
        field.errors = []
        if (field.value === '') {
          field.errors.push(`${field.name} is required.`)
        } else if (field.type === 'email' && !this.emailIsValid(field.value)) {
          field.errors.push(`${field.name} is not valid.`)
        }

        if (field.errors.length) {
          field.hasError = true;
          this.form.hasErrors = true;
        } else {
          this.form.data[fieldName] = field.value
        }
      },
      checkForm(e) {
        e.preventDefault()
        for (let key in this.form.fields) {
          this.checkField(this.form.fields[key], key)
        }
        if (!this.form.hasErrors) {
          ContactDataService.createContactMe(this.form.data)
            .then(response => {
              if (response.status == 200) {
                this.resetForm();
                this.$swal({
                  toast: true,
                  position: 'top-end',
                  showConfirmButton: false,
                  timer: 3000,
                  icon: 'success',
                  text: 'Thank you!',
                });
              }
            })
            .catch(error => {
              const errors = error.response.data
              for (let key in errors) {
                this.form.fields[key].errors = errors[key]
              }
            })
        }
      }
    }
  }
</script>

<style scoped>

</style>
