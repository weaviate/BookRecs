import '../styles/globals.css'
import type { AppProps } from 'next/app'
import Script from "next/script";

function MyApp({ Component, pageProps }: AppProps) {
  return (
    <>

        <script async src="https://www.googletagmanager.com/gtag/js?id=G-P9QFZP1Q1V"></script>
        <Script strategy="lazyOnload" id="gtag-config">
          {`
            window.dataLayer = window.dataLayer || [];
            function gtag(){dataLayer.push(arguments);}
            gtag('js', new Date());
            gtag('config', 'G-P9QFZP1Q1V');
          `}
        </Script>

      <Component {...pageProps} />
    </>
  )
  
}

export default MyApp
