def customize(utils):
  utils.copy2dir('FieldCustomizations.qll', 'qlpacks/codeql/java-all/*/')
  utils.append('import.append', 'qlpacks/codeql/java-all/*/Customizations.qll')
  utils.rebuild_packs('qlpacks/codeql/java-queries/[0-9]*.[0-9]*.[0-9]*/')
  utils.run_tests('qltest')
