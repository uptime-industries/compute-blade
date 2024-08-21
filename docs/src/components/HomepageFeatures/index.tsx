import clsx from 'clsx';
import Heading from '@theme/Heading';
import styles from './styles.module.css';

type FeatureItem = {
  title: string;
  Svg: React.ComponentType<React.ComponentProps<'svg'>>;
  description: JSX.Element;
};

const FeatureList: FeatureItem[] = [
  {
    title: 'HOME LABS',
    Svg: require('@site/static/img/home/home-labs-pix.svg').default,
    description: (
      <>
        An enterprise-level homelab experience that you can use to build, play with, and explore new technologies
      </>
    ),
  },
  {
    title: 'EDGE SERVERS',
    Svg: require('@site/static/img/home/edge-servers-pix.svg').default,
    description: (
      <>
        Reduce latency and extend compute power to make your processes leaner, more efficient, and more cost-effective.
      </>
    ),
  },
  {
    title: 'EDUCATION',
    Svg: require('@site/static/img/home/education-pix.svg').default,
    description: (
      <>
        Enhance educational experiences with practical, hands-on tech learning, facilitating innovation and computing skills.
      </>
    ),
  },
];

function Feature({title, Svg, description}: FeatureItem) {
  return (
    <div className={clsx('col col--4')}>
      <div className="text--center">
        <Svg className={styles.featureSvg} role="img" />
      </div>
      <div className="text--center padding-horiz--md">
        <Heading as="h3">{title}</Heading>
        <p>{description}</p>
      </div>
    </div>
  );
}

export default function HomepageFeatures(): JSX.Element {
  return (
    <section className={styles.features}>
      <div className="container">
        <div className="row">
          {FeatureList.map((props, idx) => (
            <Feature key={idx} {...props} />
          ))}
        </div>
      </div>
    </section>
  );
}
