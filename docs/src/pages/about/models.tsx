import useIsBrowser from '@docusaurus/useIsBrowser';
function body() {
  const isBrowser = useIsBrowser();
  const path = `https://github.com/uptime-industries/compute-blade/tree/main/bladerunner`
  const location = isBrowser ? window.location.href=path : path;
  return location;
}

export default body