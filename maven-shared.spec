%global pkg_name maven-shared
%{?scl:%scl_package %{pkg_name}}
%{?maven_find_provides_and_requires}

# Copyright (c) 2000-2005, JPackage Project
# All rights reserved.
#
# Redistribution and use in source and binary forms, with or without
# modification, are permitted provided that the following conditions
# are met:
#
# 1. Redistributions of source code must retain the above copyright
#    notice, this list of conditions and the following disclaimer.
# 2. Redistributions in binary form must reproduce the above copyright
#    notice, this list of conditions and the following disclaimer in the
#    documentation and/or other materials provided with the
#    distribution.
# 3. Neither the name of the JPackage Project nor the names of its
#    contributors may be used to endorse or promote products derived
#    from this software without specific prior written permission.
#
# THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS
# "AS IS" AND ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT
# LIMITED TO, THE IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS FOR
# A PARTICULAR PURPOSE ARE DISCLAIMED. IN NO EVENT SHALL THE COPYRIGHT
# OWNER OR CONTRIBUTORS BE LIABLE FOR ANY DIRECT, INDIRECT, INCIDENTAL,
# SPECIAL, EXEMPLARY, OR CONSEQUENTIAL DAMAGES (INCLUDING, BUT NOT
# LIMITED TO, PROCUREMENT OF SUBSTITUTE GOODS OR SERVICES; LOSS OF USE,
# DATA, OR PROFITS; OR BUSINESS INTERRUPTION) HOWEVER CAUSED AND ON ANY
# THEORY OF LIABILITY, WHETHER IN CONTRACT, STRICT LIABILITY, OR TORT
# (INCLUDING NEGLIGENCE OR OTHERWISE) ARISING IN ANY WAY OUT OF THE USE
# OF THIS SOFTWARE, EVEN IF ADVISED OF THE POSSIBILITY OF SUCH DAMAGE.
#

Summary:        Maven Shared Components
URL:            http://maven.apache.org/shared/
Name:           %{?scl_prefix}%{pkg_name}
Version:        19
Release:        4.12%{?dist}
License:        ASL 2.0

Source0:        https://github.com/apache/%{pkg_name}/archive/%{pkg_name}-components-%{version}.tar.gz

BuildRequires:  %{?scl_prefix}maven-local

BuildArch:      noarch

# Obsoleting retired subpackages. The packages with hardcoded versions and
# releases had their versions manually set in maven-shared-15 to something else
# than {version}. To make the change effective, the release below is one
# greater than the last release of maven-shared-15 in rawhide.

%description
Maven Shared Components

%prep
%setup -q -n %{pkg_name}-%{pkg_name}-components-%{version}
%{?scl:scl enable %{scl} - <<"EOF"}
set -e -x
chmod -R go=u-w *

# Maven-scm-publish-plugin is not in Fedora
%pom_remove_plugin org.apache.maven.plugins:maven-scm-publish-plugin
%{?scl:EOF}

%build
%{?scl:scl enable %{scl} - <<"EOF"}
set -e -x
%mvn_build
%{?scl:EOF}

%install
%{?scl:scl enable %{scl} - <<"EOF"}
set -e -x
%mvn_install
%{?scl:EOF}

%files -f .mfiles
%dir %{_mavenpomdir}/%{pkg_name}
%doc LICENSE.txt NOTICE.txt

%changelog
* Mon Feb 08 2016 Michal Srb <msrb@redhat.com> - 19-4.12
- Fix BR on maven-local & co.

* Mon Jan 11 2016 Michal Srb <msrb@redhat.com> - 19-4.11
- maven33 rebuild #2

* Sat Jan 09 2016 Michal Srb <msrb@redhat.com> - 19-4.10
- maven33 rebuild

* Thu Jan 15 2015 Michal Srb <msrb@redhat.com> - 19-4.9
- Fix directory ownership

* Tue Jan 13 2015 Michael Simacek <msimacek@redhat.com> - 19-4.8
- Mass rebuild 2015-01-13

* Tue Jan 06 2015 Michael Simacek <msimacek@redhat.com> - 19-4.7
- Mass rebuild 2015-01-06

* Mon May 26 2014 Mikolaj Izdebski <mizdebsk@redhat.com> - 19-4.6
- Mass rebuild 2014-05-26

* Wed Feb 19 2014 Mikolaj Izdebski <mizdebsk@redhat.com> - 19-4.5
- Mass rebuild 2014-02-19

* Tue Feb 18 2014 Mikolaj Izdebski <mizdebsk@redhat.com> - 19-4.4
- Mass rebuild 2014-02-18

* Tue Feb 18 2014 Mikolaj Izdebski <mizdebsk@redhat.com> - 19-4.3
- Rebuild to fix incorrect auto-requires

* Thu Feb 13 2014 Mikolaj Izdebski <mizdebsk@redhat.com> - 19-4.2
- Rebuild to regenerate auto-requires

* Tue Feb 11 2014 Mikolaj Izdebski <mizdebsk@redhat.com> - 19-4.1
- First maven30 software collection build

* Fri Dec 27 2013 Daniel Mach <dmach@redhat.com> - 19-4
- Mass rebuild 2013-12-27

* Tue Feb 26 2013 Tomas Radej <tradej@redhat.com> - 19-3
- Fixed obsoletions

* Wed Feb 20 2013 Tomas Radej <tradej@redhat.com> - 19-2
- Removed maven-scm-publish-plugin

* Tue Feb 19 2013 Tomas Radej <tradej@redhat.com> - 19-1
- Updated to latest upstream version
- Build with xmvn

* Thu Feb 14 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 15-31
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Wed Feb 06 2013 Java SIG <java-devel@lists.fedoraproject.org> - 15-30
- Update for https://fedoraproject.org/wiki/Fedora_19_Maven_Rebuild
- Replace maven BuildRequires with maven-local

* Thu Dec 20 2012 Michal Srb <msrb@redhat.com> - 15-29
- Migrated from maven-doxia to doxia subpackages (Resolves: #889148)

* Wed Dec 19 2012 Tomas Radej <tradej@redhat.com> - 15-28
- Obsoleted retired packages
- Sorted (B)Rs, added R on jpackage-utils

* Fri Nov 30 2012 Tomas Radej <tradej@redhat.com> - 15-27
- Removed ant, artifact-resolver, common-artifact-filters, dependency-tree, model-converter, runtime
- Replaced patches with pom macros

* Thu Nov 22 2012 Jaromir Capik <jcapik@redhat.com> - 15-26
- Migration to plexus-containers-container-default

* Mon Nov 19 2012 Mikolaj Izdebski <mizdebsk@redhat.com> - 15-25
- Fix verifier License tag
- Install licelse files

* Thu Jul 19 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 15-24
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Wed Feb 29 2012 Stanislav Ochotnicky <sochotnicky@redhat.com> 15-23
- Remove exact version dependency on artifact-filters
- Fix missing plexus-container-default in pom for shared-jar

* Sat Jan 14 2012 Ville Skyttä <ville.skytta@iki.fi> - 15-22
- Require apache-commons-validator instead of jakarta-* in reporting-impl.

* Fri Jan 13 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 15-21
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Sun Nov 27 2011 Ville Skyttä <ville.skytta@iki.fi> - 15-20
- Fix plugin-testing-harness dependency/obsoletes/provides versions.

* Wed Oct 12 2011 Jaromir Capik <jcapik@redhat.com> - 15-19
- aqute-bndlib renamed to aqute-bnd (fixing name conflict)

* Wed Aug 31 2011 Stanislav Ochotnicky <sochotnicky@redhat.com> - 15-18
- Remove filtering subpackage (separate package now)

* Mon Aug 22 2011 Jaromir Capik <jcapik@redhat.com> - 15-17
- Migration from plexus-maven-plugin to plexus-containers-component-metadata
- Minor spec file changes according to the latest guidelines

* Thu Jun 23 2011 Stanislav Ochotnicky <sochotnicky@redhat.com> - 15-16
- Add second groupId for reporting-api to add compatibility
- Versionless javadocs and remove defattr macros (not needed anymore)
- Use new maven2 compatibility packages
- Remove old patches

* Fri Jun 3 2011 Alexander Kurtakov <akurtako@redhat.com> 15-15
- Require maven not maven2 now.
- Adapt to current guidelines.

* Tue Feb 08 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 15-14
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Fri Dec 17 2010 Alexander Kurtakov <akurtako@redhat.com> 15-13
- Drop versioned jars.
- Drop tomcat5 deps.

* Thu Sep 16 2010 Stanislav Ochotnicky <sochotnicky@redhat.com> - 15-12
- Use %%global instead of %%define
- Use %%{_mavenpomdir}
- Remove plexus-registry from BR/R

* Tue Jun 01 2010 Yong Yang <yyang@redhat.com> 15-11
- Rebuld with maven221
- Add patches
- Use javadoc:aggregate

* Tue Jun 01 2010 Yong Yang <yyang@redhat.com> 15-10
- Fix installed jar name of artifact-resolver, filtering, reporting-api, runtime

* Mon May 31 2010 Alexander Kurtakov <akurtako@redhat.com> 15-9
- Reenable reporting api.
- Fix groups.
- Do not remove tests that run now.

* Mon May 31 2010 Alexander Kurtakov <akurtako@redhat.com> 15-8
- Fix maven-archiver depmap.

* Mon May 31 2010 Alexander Kurtakov <akurtako@redhat.com> 15-7
- Release should be bigger than version 8 release.

* Thu May 21 2010 Yong Yang <yyang@redhat.com> 15-1
- Upgrade to 15

* Thu May 20 2010 Yong Yang <yyang@redhat.com> 8-6
- Properly comment %%add_maven_depmap

* Thu May 20 2010 Yong Yang <yyang@redhat.com> 8-5
- Remove plugin-tools* and pluging-testing*
- Add BRs:  objectweb-asm, plexus-digest

* Thu Nov 26 2009 Lubomir Rintel <lkundrak@v3.sk> 8-4
- Fix build

* Tue Sep 01 2009 Andrew Overholt <overholt@redhat.com> 8-3
- Add tomcat5, easymock, and maven2-plugin-source BRs

* Tue Sep 01 2009 Andrew Overholt <overholt@redhat.com> 8-2
- Add tomcat5-servlet-2.4-api BR

* Mon Aug 31 2009 Andrew Overholt <overholt@redhat.com> 8-1
- Update to version 8 (courtesy Deepak Bhole)

* Wed Jul  9 2008 Tom "spot" Callaway <tcallawa@redhat.com> - 1.0-4.6
- drop repotag

* Thu May 29 2008 Tom "spot" Callaway <tcallawa@redhat.com> 1.0-4jpp.5
- fix license tag

* Thu Feb 28 2008 Deepak Bhole <dbhole@redhat.com> 1.0-4jpp.4
- Rebuild

* Fri Sep 21 2007 Deepak Bhole <dbhole@redhat.com> 0:1.0-4jpp.3
- Rebuild with ppc64 excludearch'd
- Removed 'jpp' from a BR version

* Tue Mar 20 2007 Deepak Bhole <dbhole@redhat.com> 0:1.0-4jpp.2
- Fixed BRs and Reqa

* Tue Feb 27 2007 Tania Bento <tbento@redhat.com> 0:1.0-4jpp.1
- Fixed %%Release.
- Fixed %%BuildRoot.
- Removed %%Vendor.
- Removed %%Distribution.
- Removed %%post and %%postun sections for file-management-javadoc.
- Removed %%post and %%postun sections for plugin-testing-harness-javadoc.
- Defined _with_gcj_support and gcj_support.
- Fixed %%License.
- Fixed %%Group.
- Marked config file with %%config(noreplace) in %%files section.
- Fixed instructions on how to generate source drop.

* Fri Oct 27 2006 Deepak Bhole <dbhole@redhat.com> 1.0-4jpp
- Update for maven 9jpp

* Fri Sep 15 2006 Deepak Bhole <dbhole@redhat.com> 1.0-3jpp
- Removed the file-management-pom.patch (no longer required)
- Install poms

* Wed Sep 13 2006 Ralph Apel <r.apel@r-apel.de> 0:1.0-2jpp
- Add plugin-testing-harness subpackage

* Mon Sep 11 2006 Ralph Apel <r.apel@r-apel.de> 0:1.0-1jpp
- First release
- Add gcj_support option
- Add post/postun Requires for javadoc
