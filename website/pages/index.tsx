import React from "react";
import Head from "next/head";
import Image from "next/image";

const Home: React.FC = () => {
  return (
    <div className="bg-dark text-white h-screen flex flex-col overflow-hidden">
      <Head>
        <title>BLAST - Browser-LLM Auto-Scaling Technology</title>
        <link rel="icon" href="/favicon.svg" type="image/svg+xml" />
      </Head>

      <main className="flex-1 flex items-center justify-center">
        <div className="max-w-6xl w-full mx-auto px-6 text-center">
          <div className="relative w-4/5 mx-auto aspect-video">
            <Image
              src="/assets/blast_ui_gif.gif"
              alt="BLAST Demo"
              fill
              className="rounded-lg shadow-2xl"
              style={{ objectFit: "contain" }}
              priority
            />
          </div>
          <h1 className="text-3xl md:text-2xl font-bold my-12 max-w-3xl mx-auto">
            A high-performance serving engine for web browsing AI.
          </h1>
          <div className="flex flex-wrap justify-center gap-4">
            <a
              href="https://www.lgcns.com"
              className="bg-blast-yellow text-black px-6 py-3 rounded-lg font-medium hover:opacity-90 flex items-center gap-2"
            >
              Website
            </a>
          </div>
        </div>
      </main>
    </div>
  );
};

export default Home;
