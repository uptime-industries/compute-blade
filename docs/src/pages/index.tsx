// import clsx from 'clsx';
// import Link from '@docusaurus/Link';
// import useDocusaurusContext from '@docusaurus/useDocusaurusContext';
// import Layout from '@theme/Layout';
// import HomepageFeatures from '@site/src/components/HomepageFeatures';
// import Heading from '@theme/Heading';

// import styles from './index.module.css';

// function HomepageHeader() {
//   const {siteConfig} = useDocusaurusContext();
//   return (
//     <header className={clsx('hero hero--primary', styles.heroBanner)}>
//       <div className="container">
//         <Heading as="h1" className="hero__title">
//           {siteConfig.title}
//         </Heading>
//         <p className="hero__subtitle">{siteConfig.tagline}</p>
//         <div className={styles.buttons}>
//           <Link
//             className="button button--secondary button--lg"
//             to="/docs/guides/getting-started">
//             Gettting Started
//           </Link>
//         </div>
//       </div>
//     </header>
//   );
// }

// export default function Home(): JSX.Element {
//   const {siteConfig} = useDocusaurusContext();
//   return (
//     <Layout
//       title={`Hello from ${siteConfig.title}`}
//       description="Description will go into a meta tag in <head />">
//       <HomepageHeader />
//       <main>
//         <HomepageFeatures />
//       </main>
//     </Layout>
//   );
// }

import { Redirect } from '@docusaurus/router';
import config from '../../docusaurus.config'
function Home() {
  const path = `${config.baseUrl}intro`
  return <Redirect to={path} />;
}

export default Home;
