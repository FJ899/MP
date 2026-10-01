# M2-01 Pixel and PNG Hash Evidence

| Sample | Source RGB24 SHA-256 | Saved PNG decoded RGB24 SHA-256 | PNG file SHA-256 |
|---|---|---|---|
| p10 | 0d93db5b47abe64cff7ac5bd1655c1a152f6232862f456f7e583ba81c085dd42 | 0d93db5b47abe64cff7ac5bd1655c1a152f6232862f456f7e583ba81c085dd42 | 9f54b5b6afcd4fe25f7c0f88516d762dce0267f70fa2271a14f6c1fcb90f4f25 |
| p30 | 92e3c84f2068ba763e6cd0de596c1e13e9ec40452f37315b361c524fa74f98dc | 92e3c84f2068ba763e6cd0de596c1e13e9ec40452f37315b361c524fa74f98dc | f38959261c4602ccd2a5bb2160ea56b5bcf76435b131e5414737d0dec0e33b72 |
| p50 | 5d51447c5db413e2e49037e3802076c06b6b369ed8bc6fed998ca36d16e0f1cc | 5d51447c5db413e2e49037e3802076c06b6b369ed8bc6fed998ca36d16e0f1cc | 52b91b7193b22fcdcf904d84affb700dcf1a29c2603fc658278e3c5edd077f05 |
| p70 | d027f82bb3808914f0e5649738b81cf2ec56282f7928ee9178e163bba3a4d9d7 | d027f82bb3808914f0e5649738b81cf2ec56282f7928ee9178e163bba3a4d9d7 | a1af4014c1413d24127e159b311c9c900e75dfeab7a0601b89e4502c11fe94f3 |
| p90 | dd59b335099a9173fa66525be80f86cdecb1bf0d13c2c345ae113ea08a71ac4b | dd59b335099a9173fa66525be80f86cdecb1bf0d13c2c345ae113ea08a71ac4b | 82e751dfda9e697293f8333b603dc6c36d9f9b0efae86764e438142188d28221 |

For every sample:
- Run A source RGB24 == Run B source RGB24.
- Run A saved-PNG decoded RGB24 == corresponding Run A source RGB24.
- Run B saved-PNG decoded RGB24 == corresponding Run B source RGB24.
- decoded dimensions are 3840x2160 in both runs.
- Run A PNG file SHA-256 == Run B PNG file SHA-256.
