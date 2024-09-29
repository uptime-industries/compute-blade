import { Redirect } from '@docusaurus/router';
import config from '../../docusaurus.config'
function body() {
  const path = `${config.baseUrl}datasheets`
  return <Redirect to={path} />;
}

export default body