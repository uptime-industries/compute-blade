import { Redirect } from '@docusaurus/router';
import config from '../../docusaurus.config'
function body() {
  const path = `${config.baseUrl}blade/bladerunner`
  return <Redirect to={path} />;
}

export default body