# ozi-templates CHANGELOG
## 2.5.0 (2024-07-07)


### ✨ Implemented Features

*  update for OZI spec 0.5 — rjdbcm &lt;rjdbcm@outlook.com&gt;
([`6363eaa`](https://github.com/OZI-Project/ozi-templates/commit/6363eaa0b3c35f3519add1b2f2cf37e2a283e85d))

## 2.4.9 (2024-07-04)


### 🚸 Improved Usability

*  add release pattern matching default OZI workflow to semantic_release config template — Eden Ross Duff, MSc &lt;rjdbcm@outlook.com&gt;
([`0351743`](https://github.com/OZI-Project/ozi-templates/commit/035174311c70af5986c96d1ce188d620b904ab04))

## 2.4.8 (2024-07-03)


### 🐛 Fixed Bugs

*  release patch fixes for names
([`790e648`](https://github.com/OZI-Project/ozi-templates/commit/790e648971a020f2c71095efdfae7ea5a5da7e70))


### Other


* fix: Non-lowercase and underscored name expected for ``project.name`` context — rjdbcm &lt;rjdbcm@outlook.com&gt;
([`e9feb82`](https://github.com/OZI-Project/ozi-templates/commit/e9feb82ded67eed301cc4b022ad09f82cb8c17a7))

* fix(CHANGELOG): add project name to heading

release
([`fb7dcb3`](https://github.com/OZI-Project/ozi-templates/commit/fb7dcb3ddbb64172ce989fa0790f891c152f1f41))

* Update CHANGELOG.md.j2 — Eden Ross Duff, MSc &lt;rjdbcm@outlook.com&gt;
([`727eb6c`](https://github.com/OZI-Project/ozi-templates/commit/727eb6ce0ead15df9202a6a8a30c642762b5b3b1))

## 2.4.7 (2024-07-03)


### 🐛 Fixed Bugs

*  consistent CHANGELOG style, initial 0.0.0 entry no longer overwritten by semantic-release — rjdbcm &lt;rjdbcm@outlook.com&gt;
([`c42b863`](https://github.com/OZI-Project/ozi-templates/commit/c42b8634343566fe3ab633ffa789f04a1ec1cf0f))

## 2.4.6 (2024-07-03)


### 🐛 Fixed Bugs

*  fix duplicated changelog commit headings — rjdbcm &lt;rjdbcm@outlook.com&gt;
([`4e04403`](https://github.com/OZI-Project/ozi-templates/commit/4e04403ae80ac37cc64f4b9550fe292b81b661cd))

## 2.4.5 (2024-07-03)


### 🐛 Fixed Bugs

*  fix requirements.in render to properly ignore newlines — rjdbcm &lt;rjdbcm@outlook.com&gt;
([`2e04d1a`](https://github.com/OZI-Project/ozi-templates/commit/2e04d1a99bf41b732246896211b08dccfdafb6d1))


### 🚸 Improved Usability

*  remove CHANGELOG.md from build files — rjdbcm &lt;rjdbcm@outlook.com&gt;
([`b5a89ae`](https://github.com/OZI-Project/ozi-templates/commit/b5a89ae32d5c6c12188e2f7306a359cdef358599))

## 2.4.4 (2024-07-03)


### 🐛 Fixed Bugs

*  fix nesting issue in CHANGELOG template — rjdbcm &lt;rjdbcm@outlook.com&gt;
([`92a1954`](https://github.com/OZI-Project/ozi-templates/commit/92a1954eaa44197112abbd8760836b068849bd49))

*  fix changelog template
([`2c0936c`](https://github.com/OZI-Project/ozi-templates/commit/2c0936c9c8e1fda135acf5ceeafb8fc3f4a9b402))


### Other


* Update CHANGELOG.md.j2 — Eden Ross Duff, MSc &lt;rjdbcm@outlook.com&gt;
([`ae69e8d`](https://github.com/OZI-Project/ozi-templates/commit/ae69e8d6df037bd2101879111f3159fd63d7c447))

## 2.4.3 (2024-07-03)


### 🐛 Fixed Bugs

*  escape raw jinja2 in changelog template — rjdbcm &lt;rjdbcm@outlook.com&gt;
([`3473956`](https://github.com/OZI-Project/ozi-templates/commit/347395685a96db7d5beef7a678fa57e668b0a6d4))

## 2.4.2 (2024-07-02)


### 🚸 Improved Usability

* Update ``CHANGELOG.md.j2`` to replace gitmoji codes with unicode characters. — rjdbcm &lt;rjdbcm@outlook.com&gt;
([`afa3f4d`](https://github.com/OZI-Project/ozi-templates/commit/afa3f4d9cc32170cfa297cb80ea21c48353578b1))

## 2.4.1 (2024-07-02)


### ⬆️ Upgraded Dependencies

*  Bump github/codeql-action from 3.25.10 to 3.25.11

Bumps [github/codeql-action](https://github.com/github/codeql-action) from 3.25.10 to 3.25.11.
- [Release notes](https://github.com/github/codeql-action/releases)
- [Changelog](https://github.com/github/codeql-action/blob/main/CHANGELOG.md)
- [Commits](https://github.com/github/codeql-action/compare/23acc5c183826b7a8a97bce3cecc52db901f8251...b611370bb5703a7efb587f9d136a52ea24c5c38c)


updated-dependencies:
- dependency-name: github/codeql-action
  dependency-type: direct:production
  update-type: version-update:semver-patch
... — dependabot[bot] &lt;support@github.com&gt;
([`84906bf`](https://github.com/OZI-Project/ozi-templates/commit/84906bf6a063545bac2567d810abc036918ecad9))


### 🚸 Improved Usability

* (license): add BlueOak-1.0.0 templates — rjdbcm &lt;rjdbcm@outlook.com&gt;
([`888f02d`](https://github.com/OZI-Project/ozi-templates/commit/888f02d18a1297413b0ece695508aea549d80106))

## 2.4.0 (2024-07-01)


### ✨ Implemented Features

* (license): add CeCILL-B, CeCILL-C, MirOS, OGTSL, and UPL-1.0 support.

Also fixes unlicense. — rjdbcm &lt;rjdbcm@outlook.com&gt;
([`334da31`](https://github.com/OZI-Project/ozi-templates/commit/334da31a55bc845dfddbebde1f5acc635057a66c))

## 2.3.4 (2024-06-30)


### 🐛 Fixed Bugs

*  fix missing unlicense — rjdbcm &lt;rjdbcm@outlook.com&gt;
([`eed9ec6`](https://github.com/OZI-Project/ozi-templates/commit/eed9ec690af111fc439d2f46bdf60f1a65f20492))

## 2.3.3 (2024-06-30)


### 🐛 Fixed Bugs

*  fix missing Eiffel and 0BSD license folders — rjdbcm &lt;rjdbcm@outlook.com&gt;
([`ca1ca00`](https://github.com/OZI-Project/ozi-templates/commit/ca1ca0094577a5b605a2c3b418090c91d1f671d0))

## 2.3.2 (2024-06-29)


### 🐛 Fixed Bugs

*  add missing Eiffel_Forum_License__EFL_ folder to install — rjdbcm &lt;rjdbcm@outlook.com&gt;
([`f129ef2`](https://github.com/OZI-Project/ozi-templates/commit/f129ef236951d1875d7d608681f7ca39f1b3bfde))

## 2.3.1 (2024-06-29)


### 🐛 Fixed Bugs

*  add missing EFL licenses — rjdbcm &lt;rjdbcm@outlook.com&gt;
([`f0fb24e`](https://github.com/OZI-Project/ozi-templates/commit/f0fb24e0146e741d0f2f43871b3a58c91e6cce87))

## 2.3.0 (2024-06-29)


### ✏️ Corrected Typos

*  missed comma — rjdbcm &lt;rjdbcm@outlook.com&gt;
([`59c1242`](https://github.com/OZI-Project/ozi-templates/commit/59c124291c7db9bae8c5485763ffad1dea636cba))


### ✨ Implemented Features

* (license) add all supported license variants — rjdbcm &lt;rjdbcm@outlook.com&gt;
([`2927fa1`](https://github.com/OZI-Project/ozi-templates/commit/2927fa1db28dcc63c7893aae6ee199008279bd12))

## 2.2.0 (2024-06-28)


### 🐛 Fixed Bugs

*  add ``OSI Approved :: ... Unlicense ...`` templates. — rjdbcm &lt;rjdbcm@outlook.com&gt;
([`4ec65b7`](https://github.com/OZI-Project/ozi-templates/commit/4ec65b70ddbe40717bab358c414a285b0f260249))


### ✨ Implemented Features

*  default to Unlicense for LicenseRef-Public-Domain — rjdbcm &lt;rjdbcm@outlook.com&gt;
([`14b469f`](https://github.com/OZI-Project/ozi-templates/commit/14b469fa5bbcf21ff4eccfa70c1a20899a416dca))

## 2.1.2 (2024-06-21)


### ⬆️ Upgraded Dependencies

*  Bump OZI-Project/publish from 0.1.5 to 0.1.6

Bumps [OZI-Project/publish](https://github.com/ozi-project/publish) from 0.1.5 to 0.1.6.
- [Release notes](https://github.com/ozi-project/publish/releases)
- [Commits](https://github.com/ozi-project/publish/compare/0.1.5...0.1.6)


updated-dependencies:
- dependency-name: OZI-Project/publish
  dependency-type: direct:production
  update-type: version-update:semver-patch
... — dependabot[bot] &lt;support@github.com&gt;
([`3fe734d`](https://github.com/OZI-Project/ozi-templates/commit/3fe734d2ab68217309461dae0f6bdf462bdcc88a))

*  Bump OZI-Project/draft from 0.3.2 to 0.3.3

Bumps [OZI-Project/draft](https://github.com/ozi-project/draft) from 0.3.2 to 0.3.3.
- [Release notes](https://github.com/ozi-project/draft/releases)
- [Commits](https://github.com/ozi-project/draft/compare/0.3.2...0.3.3)


updated-dependencies:
- dependency-name: OZI-Project/draft
  dependency-type: direct:production
  update-type: version-update:semver-patch
... — dependabot[bot] &lt;support@github.com&gt;
([`dec807f`](https://github.com/OZI-Project/ozi-templates/commit/dec807ff39d8b2438bc837c397e0f050cc0b4101))


### 🐛 Fixed Bugs

*  parsed_commit_heading renamed to avoid rendering — rjdbcm &lt;rjdbcm@outlook.com&gt;
([`9a8b8e1`](https://github.com/OZI-Project/ozi-templates/commit/9a8b8e17e31c6874da9be3ac82007d26db95efaa))

## 2.1.1 (2024-06-20)


### 🐛 Fixed Bugs

*  escape CHANGELOG and release notes templates — rjdbcm &lt;rjdbcm@outlook.com&gt;
([`4546e4e`](https://github.com/OZI-Project/ozi-templates/commit/4546e4e889b257bfd4fe861a1ebe6936929fe818))

## 2.1.0 (2024-06-20)


### 🐛 Fixed Bugs

* 📝 fix double escape in changelog — rjdbcm &lt;rjdbcm@outlook.com&gt;
([`a820edd`](https://github.com/OZI-Project/ozi-templates/commit/a820edd95fbea12c4c0be5198f474d07eb42f0d2))


### ✨ Implemented Features

*  add templates folder to build

The following templates are used by semantic-release:
- ``CHANGELOG.md.j2``
- ``.release_notes.md.j2``

``parsed_commit_heading.j2`` is included in both to render common commit headings. — rjdbcm &lt;rjdbcm@outlook.com&gt;
([`fff61a8`](https://github.com/OZI-Project/ozi-templates/commit/fff61a8e5279e1905c1fc104c53f3f53a4069220))

## 2.0.8 (2024-06-20)


### 🐛 Fixed Bugs

*  update wrap address in template to OZI-Project — rjdbcm &lt;rjdbcm@outlook.com&gt;
([`030351d`](https://github.com/OZI-Project/ozi-templates/commit/030351d8197881b454007790c237503e3478d58a))


### Other


* 📝 update CHANGELOG and release notes templates — rjdbcm &lt;rjdbcm@outlook.com&gt;
([`26f02d0`](https://github.com/OZI-Project/ozi-templates/commit/26f02d078ce6ad4874f97c0cba16aa9ee382930d))

## 2.0.7 (2024-06-18)


### 🚸 Improved Usability

* CHANGELOG and release_notes templates — rjdbcm &lt;rjdbcm@outlook.com&gt;
([`fa3ebef`](https://github.com/OZI-Project/ozi-templates/commit/fa3ebefbb148b70150f26f90e90aff274df66178))

## 2.0.6 (2024-06-17)


### 🐛 Fixed Bugs

* (checkpoint.yml.j2): prerelease checkpoint no longer included by default — Eden Ross Duff, MSc &lt;rjdbcm@outlook.com&gt;
([`124bc74`](https://github.com/OZI-Project/ozi-templates/commit/124bc741ca57781492785fab45d6712eee0a2fd5))


### 🚸 Improved Usability

*  Create .gitattributes — Eden Ross Duff, MSc &lt;rjdbcm@outlook.com&gt;
([`cf0ba23`](https://github.com/OZI-Project/ozi-templates/commit/cf0ba231f2e911dccf5696c9d5749cc00052f346))

## 2.0.5 (2024-06-17)


### ⬆️ Upgraded Dependencies

*  Bump ossf/scorecard-action from 2.3.1 to 2.3.3

Bumps [ossf/scorecard-action](https://github.com/ossf/scorecard-action) from 2.3.1 to 2.3.3.
- [Release notes](https://github.com/ossf/scorecard-action/releases)
- [Changelog](https://github.com/ossf/scorecard-action/blob/main/RELEASE.md)
- [Commits](https://github.com/ossf/scorecard-action/compare/0864cf19026789058feabb7e87baa5f140aac736...dc50aa9510b46c811795eb24b2f1ba02a914e534)


updated-dependencies:
- dependency-name: ossf/scorecard-action
  dependency-type: direct:production
  update-type: version-update:semver-patch
... — dependabot[bot] &lt;support@github.com&gt;
([`b8cc5cf`](https://github.com/OZI-Project/ozi-templates/commit/b8cc5cffb37316b48d63120564e0b4aca5224203))

*  Bump github/codeql-action from 3.25.3 to 3.25.10

Bumps [github/codeql-action](https://github.com/github/codeql-action) from 3.25.3 to 3.25.10.
- [Release notes](https://github.com/github/codeql-action/releases)
- [Changelog](https://github.com/github/codeql-action/blob/main/CHANGELOG.md)
- [Commits](https://github.com/github/codeql-action/compare/d39d31e687223d841ef683f52467bd88e9b21c14...23acc5c183826b7a8a97bce3cecc52db901f8251)


updated-dependencies:
- dependency-name: github/codeql-action
  dependency-type: direct:production
  update-type: version-update:semver-patch
... — dependabot[bot] &lt;support@github.com&gt;
([`ff5472f`](https://github.com/OZI-Project/ozi-templates/commit/ff5472f9f2b8d10b48bdd4c1fe061da15699e1fe))

*  Bump OZI-Project/draft from 0.3.1 to 0.3.2

Bumps [OZI-Project/draft](https://github.com/ozi-project/draft) from 0.3.1 to 0.3.2.
- [Release notes](https://github.com/ozi-project/draft/releases)
- [Commits](https://github.com/ozi-project/draft/compare/0.3.1...0.3.2)


updated-dependencies:
- dependency-name: OZI-Project/draft
  dependency-type: direct:production
  update-type: version-update:semver-patch
... — dependabot[bot] &lt;support@github.com&gt;
([`68a5674`](https://github.com/OZI-Project/ozi-templates/commit/68a56749f240cd2a18f42c9f7bb1e8907c1b240f))

*  Bump actions/dependency-review-action from 4.2.5 to 4.3.3

Bumps [actions/dependency-review-action](https://github.com/actions/dependency-review-action) from 4.2.5 to 4.3.3.
- [Release notes](https://github.com/actions/dependency-review-action/releases)
- [Commits](https://github.com/actions/dependency-review-action/compare/5bbc3ba658137598168acb2ab73b21c432dd411b...72eb03d02c7872a771aacd928f3123ac62ad6d3a)


updated-dependencies:
- dependency-name: actions/dependency-review-action
  dependency-type: direct:production
  update-type: version-update:semver-minor
... — dependabot[bot] &lt;support@github.com&gt;
([`c1498bd`](https://github.com/OZI-Project/ozi-templates/commit/c1498bd797c36a2b03e5dc8a0f7adc5145425f21))

## 2.0.4 (2024-06-17)


### 🐛 Fixed Bugs

*  fix PackageLoader path — rjdbcm &lt;rjdbcm@outlook.com&gt;
([`888050d`](https://github.com/OZI-Project/ozi-templates/commit/888050d270d1ac02ba684ee837b3347d2f2cf310))

## 2.0.3 (2024-06-17)


### 🐛 Fixed Bugs

*  fix blastpipe reference in packageloader — rjdbcm &lt;rjdbcm@outlook.com&gt;
([`2be3d1a`](https://github.com/OZI-Project/ozi-templates/commit/2be3d1a98cd266f85f5fb8e464dc10112f091e27))

## 2.0.2 (2024-06-16)


### 🐛 Fixed Bugs

*  fix project module name
([`03f8b1e`](https://github.com/OZI-Project/ozi-templates/commit/03f8b1e630ebf02f513877248ac351436a047c15))

## 2.0.1 (2024-06-16)


### ⬆️ Upgraded Dependencies

*  OZI-Project/release@0.6.5

Ignores wheel filenames in glob for sigstore. — Eden Ross Duff, MSc &lt;rjdbcm@outlook.com&gt;
([`bbe482d`](https://github.com/OZI-Project/ozi-templates/commit/bbe482da512ab78ea4c3ebcdc92a925f4e0525df))

*  bump OZI.build
([`843f161`](https://github.com/OZI-Project/ozi-templates/commit/843f161073077b5bfafcd4f052f9055e256182a2))


### 🐛 Fixed Bugs

*  OZI.build&gt;=0.0.26

parity with blastpipe 2024.11.10 — rjdbcm &lt;rjdbcm@outlook.com&gt;
([`b57d4f6`](https://github.com/OZI-Project/ozi-templates/commit/b57d4f67aa1622ddb98ab89540b063f4924a1927))

*  project name
([`1aba880`](https://github.com/OZI-Project/ozi-templates/commit/1aba8809cef1d70bc97ff9497c65cad7b5466242))


### Other


* Update README — Eden Ross Duff, MSc &lt;rjdbcm@outlook.com&gt;
([`3efec29`](https://github.com/OZI-Project/ozi-templates/commit/3efec29e2c5efdd4745e202c631649b92f62b049))

* Update meson.build - fix project name — Eden Ross Duff, MSc &lt;rjdbcm@outlook.com&gt;
([`95719bf`](https://github.com/OZI-Project/ozi-templates/commit/95719bf0abdee4f4dc7c74a332d115868bf76c3a))

* Fix branch pattern — Eden Ross Duff, MSc &lt;rjdbcm@outlook.com&gt;
([`d221e61`](https://github.com/OZI-Project/ozi-templates/commit/d221e618bca32cdf51c7dd26bb58376825d0a05b))

## 2.0.0 (2024-06-16)


### ⬆️ Upgraded Dependencies

*  Bump step-security/harden-runner from 2.7.0 to 2.8.1

Bumps [step-security/harden-runner](https://github.com/step-security/harden-runner) from 2.7.0 to 2.8.1.
- [Release notes](https://github.com/step-security/harden-runner/releases)
- [Commits](https://github.com/step-security/harden-runner/compare/63c24ba6bd7ba022e95695ff85de572c04a18142...17d0e2bd7d51742c71671bd19fa12bdc9d40a3d6)


updated-dependencies:
- dependency-name: step-security/harden-runner
  dependency-type: direct:production
  update-type: version-update:semver-minor
... — dependabot[bot] &lt;support@github.com&gt;
([`bbc592e`](https://github.com/OZI-Project/ozi-templates/commit/bbc592eb025bdd61ee5003bd554b1f5c04b61702))

*  Bump OZI-Project/checkpoint from 0.1.5 to 0.4.2

Bumps [OZI-Project/checkpoint](https://github.com/ozi-project/checkpoint) from 0.1.5 to 0.4.2.
- [Release notes](https://github.com/ozi-project/checkpoint/releases)
- [Commits](https://github.com/ozi-project/checkpoint/compare/0.1.5...0.4.2)


updated-dependencies:
- dependency-name: OZI-Project/checkpoint
  dependency-type: direct:production
  update-type: version-update:semver-minor
... — dependabot[bot] &lt;support@github.com&gt;
([`1ad4dd1`](https://github.com/OZI-Project/ozi-templates/commit/1ad4dd1b02e628b79366f6da2e582bb7ed660dc8))

*  Bump actions/checkout from 4.1.4 to 4.1.7

Bumps [actions/checkout](https://github.com/actions/checkout) from 4.1.4 to 4.1.7.
- [Release notes](https://github.com/actions/checkout/releases)
- [Changelog](https://github.com/actions/checkout/blob/main/CHANGELOG.md)
- [Commits](https://github.com/actions/checkout/compare/0ad4b8fadaa221de15dcec353f45205ec38ea70b...692973e3d937129bcbf40652eb9f2f61becf3332)


updated-dependencies:
- dependency-name: actions/checkout
  dependency-type: direct:production
  update-type: version-update:semver-patch
... — dependabot[bot] &lt;support@github.com&gt;
([`282d6b9`](https://github.com/OZI-Project/ozi-templates/commit/282d6b96d026d2285e7699169813d853715531d1))


### 💥


*  version bump — rjdbcm &lt;rjdbcm@outlook.com&gt;
([`52b4953`](https://github.com/OZI-Project/ozi-templates/commit/52b4953eaaf9427636b4112f5f7378678b2b0a50))

*  fix release strategy
([`e40ebfb`](https://github.com/OZI-Project/ozi-templates/commit/e40ebfb305a64a15aa02f6347d8cb04f633682c3))


### 🐛 Fixed Bugs

*  update to build version with normalized metadata — rjdbcm &lt;rjdbcm@outlook.com&gt;
([`2ccbd1c`](https://github.com/OZI-Project/ozi-templates/commit/2ccbd1c2f0860f690280129b812f9dcb29bf031c))

*  publish if needs.draft.outputs.drafted == &#39;true&#39; — rjdbcm &lt;rjdbcm@outlook.com&gt;
([`244ddf4`](https://github.com/OZI-Project/ozi-templates/commit/244ddf4c8c74955689ec9a007efa6b09f9e75165))

*  fix repo name — Eden Ross Duff, MSc &lt;rjdbcm@outlook.com&gt;
([`959bab3`](https://github.com/OZI-Project/ozi-templates/commit/959bab31da5befd1e651ecb072fa7026e24cc9e9))

*  fix missing tag input to release — rjdbcm &lt;rjdbcm@outlook.com&gt;
([`a677875`](https://github.com/OZI-Project/ozi-templates/commit/a6778750e5546955daf528f22283bfb77c76fd93))

*  major_on_zero back to false — rjdbcm &lt;rjdbcm@outlook.com&gt;
([`8e76820`](https://github.com/OZI-Project/ozi-templates/commit/8e76820683aebe3f89f519ec2159ba815de7ca5c))

*  fix missing commit_parser_options — rjdbcm &lt;rjdbcm@outlook.com&gt;
([`ccf75ef`](https://github.com/OZI-Project/ozi-templates/commit/ccf75ef7f8ccc0cf99329f5a348dc45df84c536e))

*  fix commit_parser name — rjdbcm &lt;rjdbcm@outlook.com&gt;
([`26b9b7a`](https://github.com/OZI-Project/ozi-templates/commit/26b9b7a61c31170e1e77b6532d9d3ef3448a8505))


### ✨ Implemented Features

*  bump version — rjdbcm &lt;rjdbcm@outlook.com&gt;
([`83c01e5`](https://github.com/OZI-Project/ozi-templates/commit/83c01e5f8def35badc58f7b00bba58b2fa547c94))

*  revert angular commit parsing. — rjdbcm &lt;rjdbcm@outlook.com&gt;
([`1a8e395`](https://github.com/OZI-Project/ozi-templates/commit/1a8e3958989ed760de0494faef3c48797d13b3e4))


### Other


* Update pyproject.toml — Eden Ross Duff, MSc &lt;rjdbcm@outlook.com&gt;
([`178143e`](https://github.com/OZI-Project/ozi-templates/commit/178143e956bb251585181c680d1278b99cc98650))

* Update pyproject.toml — Eden Ross Duff, MSc &lt;rjdbcm@outlook.com&gt;
([`f4b6b38`](https://github.com/OZI-Project/ozi-templates/commit/f4b6b38ad98c1e22df02cf45c758fa7d664cd4ee))

* Update pyproject.toml — Eden Ross Duff, MSc &lt;rjdbcm@outlook.com&gt;
([`63eb260`](https://github.com/OZI-Project/ozi-templates/commit/63eb260f9e4a916d80d226b890f385ee1fd463ad))

* fix(semantic-release): config ``major_on_zero = true`` — rjdbcm &lt;rjdbcm@outlook.com&gt;
([`e2e04ef`](https://github.com/OZI-Project/ozi-templates/commit/e2e04efdf3d1d93868d3d1653f547427e5b63b18))

* fix(readme-renderer): fix args to target readme copied during build — rjdbcm &lt;rjdbcm@outlook.com&gt;
([`d7ed57f`](https://github.com/OZI-Project/ozi-templates/commit/d7ed57f81d679006b0cf8125ee92d68b541e15de))

* style(isort): import sort — rjdbcm &lt;rjdbcm@outlook.com&gt;
([`fad659c`](https://github.com/OZI-Project/ozi-templates/commit/fad659c29b487e507396522e5edbb08923444ca8))

* fix(dist-depends): restore requirements.in — rjdbcm &lt;rjdbcm@outlook.com&gt;
([`3586f0f`](https://github.com/OZI-Project/ozi-templates/commit/3586f0f033a1f0d52c680c7964a5ab3b1ec8b006))

* fix(imports): remove blastpipe references — rjdbcm &lt;rjdbcm@outlook.com&gt;
([`97395ae`](https://github.com/OZI-Project/ozi-templates/commit/97395ae610647f20909152613dbd927447dc418b))

* fix(tests): add test_filter.py to build — rjdbcm &lt;rjdbcm@outlook.com&gt;
([`9b99d3a`](https://github.com/OZI-Project/ozi-templates/commit/9b99d3a060de90f41f12509e68f5b50f12705a08))

* style(isort): sort imports — rjdbcm &lt;rjdbcm@outlook.com&gt;
([`6faeeff`](https://github.com/OZI-Project/ozi-templates/commit/6faeeffed15231f5f3ac6f2f8628e78b430081d6))

* Update pyproject.toml — Eden Ross Duff, MSc &lt;rjdbcm@outlook.com&gt;
([`8dfad97`](https://github.com/OZI-Project/ozi-templates/commit/8dfad9728cb2934c388714f1e9a968000993dcd1))

* feat(package): mirror blastpipe 2024.11.7 ozi_templates — rjdbcm &lt;rjdbcm@outlook.com&gt;
([`2987d9c`](https://github.com/OZI-Project/ozi-templates/commit/2987d9c6b8ebc723ed3dc39334794c7fd764709a))

## 1.0.0 (2024-04-27)


### 💥


*  add load_environment() func — rjdbcm &lt;rjdbcm@mail.umkc.edu&gt;
([`7cb9510`](https://github.com/OZI-Project/ozi-templates/commit/7cb951045f3855ab6a301ca52d536d96e4a3f0c0))


### 🐛 Fixed Bugs

*  fix release workflow outputs so publish is not skipped. — rjdbcm &lt;rjdbcm@outlook.com&gt;
([`2ce8dd0`](https://github.com/OZI-Project/ozi-templates/commit/2ce8dd0f24f52f9c497dd9dd57be6bdcd917b010))

*  Fix publish workflow had ssh arguments still. — rjdbcm &lt;rjdbcm@outlook.com&gt;
([`77a8ede`](https://github.com/OZI-Project/ozi-templates/commit/77a8edef6915fc3324e0ac131500747a5a8d72f1))

*  fix name normalization in project and template.

Without normalization we get duplicate dist_info. — rjdbcm &lt;rjdbcm@outlook.com&gt;
([`d40e46a`](https://github.com/OZI-Project/ozi-templates/commit/d40e46ae36927546cca0fe76baa2c870ccd6a2a7))


### 🔥 Deleted Code or Files

*  delete template readme
([`33abd6c`](https://github.com/OZI-Project/ozi-templates/commit/33abd6c51075136fb8b40ba7c81e28a2b405f236))


### ✏️ Corrected Typos

*  correct project name
([`9df80d8`](https://github.com/OZI-Project/ozi-templates/commit/9df80d8511050ab6596f5b10f8d7dc41be0c0924))


### Other


* Initial clone of templates — rjdbcm &lt;rjdbcm@mail.umkc.edu&gt;
([`a8370f9`](https://github.com/OZI-Project/ozi-templates/commit/a8370f94cf621f3035ce6ac956fe96a752b005d2))

* Bump github/codeql-action from 3.25.2 to 3.25.3

Bumps [github/codeql-action](https://github.com/github/codeql-action) from 3.25.2 to 3.25.3.
- [Release notes](https://github.com/github/codeql-action/releases)
- [Changelog](https://github.com/github/codeql-action/blob/main/CHANGELOG.md)
- [Commits](https://github.com/github/codeql-action/compare/8f596b4ae3cb3c588a5c46780b86dd53fef16c52...d39d31e687223d841ef683f52467bd88e9b21c14)


updated-dependencies:
- dependency-name: github/codeql-action
  dependency-type: direct:production
  update-type: version-update:semver-patch
... — dependabot[bot] &lt;support@github.com&gt;
([`54566b3`](https://github.com/OZI-Project/ozi-templates/commit/54566b3f685b0a8757105c1ff8177eabdbe61d3e))

* Initial commit
([`6df66d3`](https://github.com/OZI-Project/ozi-templates/commit/6df66d3a74d25f7e06bb573249b8c065155b9358))
