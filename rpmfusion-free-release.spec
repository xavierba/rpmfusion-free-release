%global repo free
#global repo nonfree
#global israwhide 1

Name:           rpmfusion-%{repo}-release
Version:        26
Release:        2
Summary:        RPM Fusion (%{repo}) Repository Configuration

Group:          System Environment/Base
License:        BSD
URL:            http://rpmfusion.org
Source1:        rpmfusion-%{repo}.repo
Source2:        rpmfusion-%{repo}-updates.repo
Source3:        rpmfusion-%{repo}-updates-testing.repo
Source4:        rpmfusion-%{repo}-rawhide.repo
Source5:        rpmfusion-%{repo}-tainted.repo
Source26:       RPM-GPG-KEY-rpmfusion-%{repo}-fedora-26-primary
Source27:       RPM-GPG-KEY-rpmfusion-%{repo}-fedora-27-primary
Source28:       RPM-GPG-KEY-rpmfusion-%{repo}-fedora-28-primary
BuildArch:      noarch

Requires:       system-release(%{version})
Provides:       rpmfusion-%{repo}-repos(%{version})

%if 0%{?israwhide}
Obsoletes:      %{name}-rawhide < %{version}-%{release}
Provides:       %{name}-rawhide = %{version}-%{release}
%endif

%description
RPM Fusion %{repo} package repository files for yum and dnf
along with gpg public keys


%if ! 0%{?israwhide}
%package rawhide
Summary:        RPM Fusion Rawhide %{repo} repo definitions
Requires:       %{name} = %{version}-%{release}

%description rawhide
This package provides the RPM Fusion rawhide %{repo} repo definitions.
%endif

%package tainted
Summary:        RPM Fusion %{repo} Tainted repo definition
Requires:       %{name} = %{version}-%{release}
Obsoletes:      livna-release < 1:1-2
Provides:       livna-release = 1:1-2

%description tainted
This package provides the RPM Fusion %{repo} Tainted repo definitions.

%prep
echo "Nothing to prep"

%build
echo "Nothing to build"

%install

# Create dirs
install -d -m755 \
  %{buildroot}%{_sysconfdir}/pki/rpm-gpg  \
  %{buildroot}%{_sysconfdir}/yum.repos.d

# GPG Key
%{__install} -Dp -m644 \
    %{SOURCE26} \
    %{SOURCE27} \
    %{SOURCE28} \
    %{buildroot}%{_sysconfdir}/pki/rpm-gpg

# compatibility symlink for easy transition to F11
ln -s $(basename %{SOURCE26}) %{buildroot}%{_sysconfdir}/pki/rpm-gpg/RPM-GPG-KEY-rpmfusion-%{repo}-fedora

# Avoid using basearch in name for the key. Introduced in F18
ln -s $(basename %{SOURCE26}) %{buildroot}%{_sysconfdir}/pki/rpm-gpg/RPM-GPG-KEY-rpmfusion-%{repo}-fedora-26
ln -s $(basename %{SOURCE27}) %{buildroot}%{_sysconfdir}/pki/rpm-gpg/RPM-GPG-KEY-rpmfusion-%{repo}-fedora-27
ln -s $(basename %{SOURCE28}) %{buildroot}%{_sysconfdir}/pki/rpm-gpg/RPM-GPG-KEY-rpmfusion-%{repo}-fedora-28

# Links for the keys
ln -s $(basename %{SOURCE27}) %{buildroot}%{_sysconfdir}/pki/rpm-gpg/RPM-GPG-KEY-rpmfusion-%{repo}-fedora-latest
ln -s $(basename %{SOURCE28}) %{buildroot}%{_sysconfdir}/pki/rpm-gpg/RPM-GPG-KEY-rpmfusion-%{repo}-fedora-rawhide


# Yum .repo files
%{__install} -p -m644 \
    %{SOURCE1} \
    %{SOURCE2} \
    %{SOURCE3} \
    %{SOURCE4} \
    %{SOURCE5} \
    %{buildroot}%{_sysconfdir}/yum.repos.d


%files
%config %{_sysconfdir}/pki/rpm-gpg/*
%config(noreplace) %{_sysconfdir}/yum.repos.d/rpmfusion-%{repo}.repo
%config(noreplace) %{_sysconfdir}/yum.repos.d/rpmfusion-%{repo}-updates*.repo

%if ! 0%{?israwhide}
%files rawhide
%endif
%config(noreplace) %{_sysconfdir}/yum.repos.d/rpmfusion-%{repo}-rawhide.repo

%files tainted
%config(noreplace) %{_sysconfdir}/yum.repos.d/rpmfusion-%{repo}-tainted.repo

%changelog
* Mon Mar 19 2018 Xavier Bachelot <xavier@bachelot.org> - 26-2
- Create sub-package for tainted repo.

* Fri Jul 07 2017 Nicolas Chauvet <kwizart@gmail.com> - 26-1
- Update to Final

* Tue Mar 28 2017 Nicolas Chauvet <kwizart@gmail.com> - 26-0.6
- Branch layout

* Tue Mar 28 2017 Nicolas Chauvet <kwizart@gmail.com> - 26-0.5
- Add Zypper compatibility, patch by Neal Gompa - rfbz#4481

* Fri Nov 18 2016 Nicolas Chauvet <kwizart@gmail.com> - 26-0.4
- Add f26/f27 keys
- Remove f23/f24 keys
- Clean-up Description
- Improve Requires/Provides
- Drop dependency on free from nonfree
- Add a rawhide sub-package - rfbz#3223
- Mark gpg keys as %%config

* Wed Nov 02 2016 Nicolas Chauvet <kwizart@gmail.com> - 26-0.3
- Add metalink over https

* Wed Aug 24 2016 Sérgio Basto <sergio@serjux.com> - 26-0.2
- Fix current symlink and f25 symlink

* Sat Aug 06 2016 Nicolas Chauvet <kwizart@gmail.com> - 26-0.1
- Bump for f26

* Fri Jun 24 2016 Nicolas Chauvet <kwizart@gmail.com> - 25-0.2
- Bump for rawhide release

* Sun May 15 2016 Nicolas Chauvet <kwizart@gmail.com> - 25-0.1
- Update to 25

* Sat May 14 2016 Nicolas Chauvet <kwizart@gmail.com> - 24-0.1
- Update to 24

* Sat Oct 24 2015 Nicolas Chauvet <kwizart@gmail.com> - 23-0.1
- Bump for branched/f23

* Sat May 23 2015 Nicolas Chauvet <kwizart@gmail.com> - 22-1
- Update to Final F-22

* Tue May 05 2015 Nicolas Chauvet <kwizart@gmail.com> - 22-0.1
- Bump for branched/f22

* Mon Dec 08 2014 Nicolas Chauvet <kwizart@gmail.com> - 21-1
- Update to Final F-21

* Sun Jan 12 2014 Nicolas Chauvet <kwizart@gmail.com> - 21-0.1
- Bump for Rawhide/F-21

* Sun Dec 15 2013 Nicolas Chauvet <kwizart@gmail.com> - 20-1
- Update to f20 final

* Fri Jun 28 2013 Nicolas Chauvet <kwizart@gmail.com> - 20-0.2
- Add key for Rawhide/F-21
- Spec file clean-up

* Mon Mar 18 2013 Nicolas Chauvet <kwizart@gmail.com> - 20-0.1
- Build for Rawhide/F-20

* Thu Mar 14 2013 Nicolas Chauvet <kwizart@gmail.com> - 19-0.4
- Fix GPG's key name

* Wed Mar 13 2013 Nicolas Chauvet <kwizart@gmail.com> - 19-0.3
- Branch F-19

* Tue Jan 01 2013 Nicolas Chauvet <kwizart@gmail.com> - 19-0.2
- Add key for Rawhide/F-20

* Mon Aug 20 2012 Nicolas Chauvet <kwizart@gmail.com> - 19-0.1
- Build for Rawhide/F-19

* Wed Aug 08 2012 Nicolas Chauvet <kwizart@gmail.com> - 18-0.2
- Bump for Branched/F-18

* Fri May 18 2012 Nicolas Chauvet <kwizart@gmail.com> - 18-0.1
- Build for Rawhide/F-18

* Fri May 18 2012 Nicolas Chauvet <kwizart@gmail.com> - 17-1
- Update to final 17

* Tue Mar 06 2012 Nicolas Chauvet <kwizart@gmail.com> - 17-0.5
- Bump

* Mon Feb 27 2012 Nicolas Chauvet <kwizart@gmail.com> - 17-0.4
- Split to development/17
- Enable rpmfusion*-updates-testing

* Sat Feb 11 2012 Nicolas Chauvet <kwizart@gmail.com> - 17-0.3
- Bump for branched F-17

* Sat Nov 19 2011 Nicolas Chauvet <kwizart@gmail.com> - 17-0.1
- build for rawhide/F-17
- Drop key for F-15

* Wed Nov 02 2011 Nicolas Chauvet <kwizart@gmail.com> - 16-1.2
- Fix compat key for F-15
- Fix Installation of F-17 key

* Thu Oct 27 2011 Nicolas Chauvet <kwizart@gmail.com> - 16-1
- Add keys for Rawhide/F-17
- Build for F-16

* Sun Jun 05 2011 Thorsten Leemhuis <fedora at leemhuis.info> - 16.1
- build for rawhide/F-16

* Sat May 28 2011 Thorsten Leemhuis <fedora at leemhuis.info> - 15-1
- Add keys for Rawhide/F16
- Build for F-15

* Sat Oct 16 2010 Thorsten Leemhuis <fedora at leemhuis.info> - 14-0.4
- drop ppc
- add key for F-15, drop the one for F-13

* Sun Oct 10 2010 Thorsten Leemhuis <fedora at leemhuis.info> - 14-0.3
- branching for F14: disable rawhide, enable everything and updates

* Mon Apr 26 2010 Thorsten Leemhuis <fedora at leemhuis.info> - 14-0.2
- fix compatibility symlink

* Sat Apr 24 2010 Thorsten Leemhuis <fedora at leemhuis.info> - 14-0.1
- rebuild for rawhide

* Fri Apr 16 2010 Thorsten Leemhuis <fedora at leemhuis.info> - 13-1
- add key for Rawhide/F14
- remove key for F12

* Sun Nov 22 2009 Thorsten Leemhuis <fedora at leemhuis.info> - 13-0.1
- Bump for Fedora 13's rawhide.
- Put the version at 13 from the start. 
- drop post script

* Sun Nov 15 2009 Thorsten Leemhuis <fedora at leemhuis.info> - 12-1
- F12 release: disable rawhide, enable everything and updates
- remove key for F11
- add key for F13

* Thu Jun 11 2009 Thorsten Leemhuis <fedora at leemhuis.info> - 11.90-1
- build for rawhide (enable rawhide, disable all the other repos)

* Sun May 17 2009 Thorsten Leemhuis <fedora at leemhuis.info> - 11-1
- F11 release: disable rawhide, enable everything and updates
- use "metadata_expire=7d" for everything repos
- Track in some changes from 10-{34} (myself):
-- remove old comments to obsolete release packages from freshrpms, dribble and livna
-- add proper links for rawhide
-- add key for F12
-- some small adjustments to the spec
-- add post script that switch old config files from serverside mirrorlists to
   mirrormanager 
- Track in some changes from 10-{23} (Till Maas):
-- fix symlinks
-- allow easy transition to F11 with new gpg key and naming structure

* Sun May 17 2009 Thorsten Leemhuis <fedora at leemhuis.info> - 10-4
- add key for F12
- some small adjustments to the spec
- add post script that switch old config files from serverside mirrorlists to
  mirrormanager

* Sat May 16 2009 Till Maas <opensource@till.name> - 10-3
- fix symlinks

* Sat May 16 2009 Till Maas <opensource@till.name> - 10-2
- allow easy transition to F11 with new gpg key and naming structure

* Sun Mar 29 2009 Thorsten Leemhuis <fedora [AT] leemhuis [DOT] info> - 10.90-3
- rebuild for new F11 features

* Sat Mar 21 2009 Thorsten Leemhuis <fedora at leemhuis.info> - 10.90-2
- add new key for SHA256 signatures
- use the same structure for keys as fedora does

* Wed Nov 26 2008 Thorsten Leemhuis <fedora at leemhuis.info> - 10.90-1
- Initial build for Fedora 11.

* Sat Nov 15 2008 Thorsten Leemhuis <fedora at leemhuis.info> - 10-1
- build for F-10

* Mon Nov 03 2008 Thorsten Leemhuis <fedora at leemhuis.info> - 9.90-5
- enable the proper mirrormanager server in the repo files

* Sat Oct 04 2008 Thorsten Leemhuis <fedora at leemhuis.info> - 9.90-4
- require system-release instead of fedora-release

* Tue Sep 30 2008 Thorsten Leemhuis <fedora at leemhuis.info> - 9.90-3
- s|download.rpmfusion.org|download1.rpmfusion.org|' *.repo
- s|basearch/debug/|basearch/os/debug/|" in *rawhide.repo

* Sun Sep 28 2008 Thorsten Leemhuis <fedora at leemhuis.info> - 9.90-2
- Fix rpmfusion-rpmfusion typo (again)
- update summary to properly say free or nonfree

* Sat Sep 27 2008 Thorsten Leemhuis <fedora at leemhuis.info> - 9.90-1
- Update for Fedora 10 rawhide
- enable devel repos, disable all the others

* Sat Sep 27 2008 Stewart Adam <s.adam at diffingo.com> - 9-7
- Use temporary mirrorlists for now, and baseurl for the debug & source repos

* Thu Sep 18 2008 Stewart Adam <s.adam at diffingo.com> - 9-6
- Fix rpmfusion-rpmfusion typo

* Mon Aug 18 2008 Stewart Adam <s.adam at diffingo.com> - 9-5
- Use mirrors.rpmfusion.org instead of rpmfusion.org/mirrorlist
- Use download.rpmfusion.org instead of download1.rpmfusion.org

* Fri Aug 15 2008 Stewart Adam <s.adam at diffingo.com> - 9-4
- Only include provides/obsoletes for pre-merger release RPMs in nonfree 
- Remove GPL doc

* Thu Aug 14 2008 Thorsten Leemhuis <fedora at leemhuis.info> - 9-3
- add conditionals and macros to use one spec file for both free and nonfree
- some cleanups

* Wed Aug 13 2008 Stewart Adam <s.adam at diffingo.com> - 9-2
- Split into free and non-free RPMs based on original release RPM
- Remove double BuildArch
- Remove GPL source
- Fix mirror URLs
- devel --> rawhide

* Tue Aug 12 2008 Stewart Adam <s.adam at diffingo.com> - 9-1
- Initial RPM release

