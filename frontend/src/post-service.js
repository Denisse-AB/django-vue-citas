import axios from 'axios'

axios.defaults.xsrfHeaderName = 'X-CSRFToken'
axios.defaults.xsrfCookieName = 'csrftoken'

const url = 'post/'

class PostService {
  static async insertPost (email, name, date, tel, time, csrftoken) {
    axios.defaults.headers.common['X-CSRFToken'] = csrftoken
    const res = await axios.post(url, {
      email, name, date, tel, time
    })
    return res
  }
}

export default PostService
