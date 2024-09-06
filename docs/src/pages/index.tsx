import clsx from 'clsx';
import Link from '@docusaurus/Link';
import useDocusaurusContext from '@docusaurus/useDocusaurusContext';
import Layout from '@theme/Layout';
import HomepageFeatures from '@site/src/components/HomepageFeatures';
import Heading from '@theme/Heading';

import styles from './index.module.css';

function HomepageHeader() {
  const {siteConfig} = useDocusaurusContext();
  return (
    <header className={clsx('hero hero--primary', styles.heroBanner)}>
      <div className="container">
        <Heading as="h1" className="hero__title">
          <span>{siteConfig.title}</span>
        </Heading>
        <p className="hero__subtitle"><span>{siteConfig.tagline}</span></p>
        <div className={styles.buttons}>
          <Link
            className="button button--secondary button--lg"
            to="/blade">
            Getting Started
          </Link>
        </div>
      </div>
    </header>
  );
}

export default function Home(): JSX.Element {
  const {siteConfig} = useDocusaurusContext();
  return (
    <Layout
      title={`${siteConfig.title}`}
      description="Documentation for Compute Blade bring the cloud home <head />">
      <HomepageHeader />
      <main>
        <HomepageFeatures />
      </main>
    </Layout>
  );
}

// import { Redirect } from '@docusaurus/router';
// import config from '../../docusaurus.config'
// function Home() {
//   const path = `${config.baseUrl}blade`
//   return <Redirect to={path} />;
// }

// export default Home;
