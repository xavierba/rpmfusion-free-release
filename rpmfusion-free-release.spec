%define repo free
#define repo nonfree

Name:           rpmfusion-%{repo}-release
Version:        7
Release:        2
Summary:        RPM Fusion (%{repo}) Repository Configuration

Group:          System Environment/Base
License:        BSD
URL:            http://rpmfusion.org
Source0:        RPM-GPG-KEY-rpmfusion-%{repo}-el-7
# not needed for now, but maybe we'll do that later:
# Source1:      rpmfusion-%{repo}.repo
Source2:        rpmfusion-%{repo}-updates.repo
Source3:        rpmfusion-%{repo}-updates-testing.repo
Source5:        rpmfusion-%{repo}-tainted.repo
BuildArch:      noarch

Requires:       redhat-release >= %{version}
Requires:       epel-release >= %{version}


%if %{repo} == "nonfree"
Requires:       rpmfusion-free-release >= %{version}

%description
RPM Fusion repository contains open source and other distributable software for
EL + EPEL. It is the merger of the Dribble, FreshRPMs and Livna repositories.

This package contains the RPM Fusion GPG key as well as Yum package manager
configuration files for RPM Fusion's "nonfree" repository, which holds
software that is not considered as Open Source Software according to the
Fedora packaging guidelines. 
%else
%description
RPM Fusion repository contains open source and other distributable software for
EL + EPEL. It is the merger of the Dribble, FreshRPMs and Livna repositories.

This package contains the RPM Fusion GPG key as well as Yum package manager
configuration files for RPM Fusion's "free" repository, which holds only
software that is considered as Open Source Software according to the Fedora
packaging guidelines. 
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
  $RPM_BUILD_ROOT%{_sysconfdir}/pki/rpm-gpg  \
  $RPM_BUILD_ROOT%{_sysconfdir}/yum.repos.d

# GPG Key
%{__install} -Dp -m644 %{SOURCE0} \
    $RPM_BUILD_ROOT%{_sysconfdir}/pki/rpm-gpg

# Yum .repo files
%{__install} -p -m644 \
    %{SOURCE2} \
    %{SOURCE3} \
    %{SOURCE5} \
    %{buildroot}%{_sysconfdir}/yum.repos.d

%files
%{_sysconfdir}/pki/rpm-gpg/*
%config(noreplace) %{_sysconfdir}/yum.repos.d/*

%files tainted
%config(noreplace) %{_sysconfdir}/yum.repos.d/rpmfusion-%{repo}-tainted.repo

%changelog
* Mon Mar 19 2018 Xavier Bachelot <xavier@bachelot.org> - 7-2
- Create sub-package for tainted repo.

* Thu Sep 15 2016 Nicolas Chauvet <kwizart@gmail.com> - 7-1
- Release for EL-7

* Tue Jun 19 2012 Nicolas Chauvet <kwizart@gmail.com> - 6-1
- Release for EL-6

* Sun May 01 2011 Robert Scheck <robert@fedoraproject.org> 6-0.1
- Initial RPM release based on Thorsten Leemhuis' work for EL-5
