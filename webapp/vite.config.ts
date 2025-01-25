// import { defineConfig } from "vite";
// import react from "@vitejs/plugin-react";
// import tailwindcss from "@tailwindcss/vite";
// import path from "path"; // Import path

// // https://vite.dev/config/
// export default defineConfig({
//     plugins: [react(), tailwindcss()],
//     resolve: {
//         alias: {
//             "@": path.resolve(__dirname, "./src"), // This is the key part
//         },
//     },
// });

import path from "node:path";
import { createRequire } from "node:module";
import { defineConfig, normalizePath } from "vite";
import { viteStaticCopy } from "vite-plugin-static-copy";
import react from "@vitejs/plugin-react";
import tailwindcss from "@tailwindcss/vite";

const require = createRequire(import.meta.url);
const cMapsDir = normalizePath(
    path.join(path.dirname(require.resolve("pdfjs-dist/package.json")), "cmaps")
);
const standardFontsDir = normalizePath(
    path.join(
        path.dirname(require.resolve("pdfjs-dist/package.json")),
        "standard_fonts"
    )
);

export default defineConfig({
    plugins: [
        viteStaticCopy({
            targets: [
                { src: cMapsDir, dest: "" },
                { src: standardFontsDir, dest: "" },
            ],
        }),
        react(),
        tailwindcss(),
    ],
    resolve: {
        alias: {
            "@": path.resolve(__dirname, "./src"), // This is the key part
        },
    },
});
