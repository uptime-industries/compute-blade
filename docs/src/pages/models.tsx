import { Redirect } from '@docusaurus/router';
import config from '../../docusaurus.config'
function body() {
  const path = `https://github.com/uptime-industries/compute-blade/tree/main/bladerunner`
  return window.location.href = path;
}

export default body