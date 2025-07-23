import useIsBrowser from '@docusaurus/useIsBrowser';
function body() {
  const isBrowser = useIsBrowser();
  const path = `https://github.com/uptime-lab/compute-blade/tree/main/models`
  const location = isBrowser ? window.location.href=path : path;
  return location;
}

export default body