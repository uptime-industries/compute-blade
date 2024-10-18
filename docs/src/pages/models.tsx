import { Redirect } from '@docusaurus/router';
import config from '../../docusaurus.config'
function body() {
  const path = `${config.baseUrl}bladerunner`
  return <Redirect to={path} />;
}

export default body