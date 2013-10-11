# revision 30011
# category Package
# catalog-ctan /language/japanese/jfontmaps
# catalog-date 2013-04-11 22:52:04 +0200
# catalog-license gpl3
# catalog-version undef
Name:		texlive-jfontmaps
Version:	20130411
Release:	1
Summary:	Font maps and configuration tools for Japanese fonts
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/language/japanese/jfontmaps
License:	GPL3
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/jfontmaps.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/jfontmaps.doc.tar.xz
Source2:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/jfontmaps.source.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea
Provides:	texlive-jfontmaps.bin = %{EVRD}

%description
The package offers font maps, and supporting material, that
make various Japanese fonts available to users of (u)ptex and
related programs or formats.

%post
    %{_sbindir}/texlive.post

%postun
    if [ $1 -eq 0 ]; then
	%{_sbindir}/texlive.post
    fi

#-----------------------------------------------------------------------
%files
%{_bindir}/updmap-setup-kanji
%{_bindir}/updmap-setup-kanji-sys
%{_texmfdistdir}/fonts/cmap/jfontmaps/2004-H
%{_texmfdistdir}/fonts/cmap/jfontmaps/2004-V
%{_texmfdistdir}/fonts/map/dvipdfmx/jfontmaps/hiragino-pron/otf-hiragino-pron.map
%{_texmfdistdir}/fonts/map/dvipdfmx/jfontmaps/hiragino-pron/otf-up-hiragino-pron.map
%{_texmfdistdir}/fonts/map/dvipdfmx/jfontmaps/hiragino-pron/ptex-hiragino-pron-04.map
%{_texmfdistdir}/fonts/map/dvipdfmx/jfontmaps/hiragino-pron/ptex-hiragino-pron.map
%{_texmfdistdir}/fonts/map/dvipdfmx/jfontmaps/hiragino-pron/uptex-hiragino-pron-04.map
%{_texmfdistdir}/fonts/map/dvipdfmx/jfontmaps/hiragino-pron/uptex-hiragino-pron.map
%{_texmfdistdir}/fonts/map/dvipdfmx/jfontmaps/hiragino/otf-hiragino.map
%{_texmfdistdir}/fonts/map/dvipdfmx/jfontmaps/hiragino/otf-up-hiragino.map
%{_texmfdistdir}/fonts/map/dvipdfmx/jfontmaps/hiragino/ptex-hiragino-04.map
%{_texmfdistdir}/fonts/map/dvipdfmx/jfontmaps/hiragino/ptex-hiragino.map
%{_texmfdistdir}/fonts/map/dvipdfmx/jfontmaps/hiragino/uptex-hiragino-04.map
%{_texmfdistdir}/fonts/map/dvipdfmx/jfontmaps/hiragino/uptex-hiragino.map
%{_texmfdistdir}/fonts/map/dvipdfmx/jfontmaps/ipa/otf-ipa.map
%{_texmfdistdir}/fonts/map/dvipdfmx/jfontmaps/ipa/otf-up-ipa.map
%{_texmfdistdir}/fonts/map/dvipdfmx/jfontmaps/ipa/ptex-ipa.map
%{_texmfdistdir}/fonts/map/dvipdfmx/jfontmaps/ipa/uptex-ipa.map
%{_texmfdistdir}/fonts/map/dvipdfmx/jfontmaps/ipaex/otf-ipaex.map
%{_texmfdistdir}/fonts/map/dvipdfmx/jfontmaps/ipaex/otf-up-ipaex.map
%{_texmfdistdir}/fonts/map/dvipdfmx/jfontmaps/ipaex/ptex-ipaex.map
%{_texmfdistdir}/fonts/map/dvipdfmx/jfontmaps/ipaex/uptex-ipaex.map
%{_texmfdistdir}/fonts/map/dvipdfmx/jfontmaps/kozuka-pr6/otf-kozuka-pr6.map
%{_texmfdistdir}/fonts/map/dvipdfmx/jfontmaps/kozuka-pr6/otf-up-kozuka-pr6.map
%{_texmfdistdir}/fonts/map/dvipdfmx/jfontmaps/kozuka-pr6/ptex-kozuka-pr6-04.map
%{_texmfdistdir}/fonts/map/dvipdfmx/jfontmaps/kozuka-pr6/ptex-kozuka-pr6.map
%{_texmfdistdir}/fonts/map/dvipdfmx/jfontmaps/kozuka-pr6/uptex-kozuka-pr6-04.map
%{_texmfdistdir}/fonts/map/dvipdfmx/jfontmaps/kozuka-pr6/uptex-kozuka-pr6.map
%{_texmfdistdir}/fonts/map/dvipdfmx/jfontmaps/kozuka-pr6n/otf-kozuka-pr6n.map
%{_texmfdistdir}/fonts/map/dvipdfmx/jfontmaps/kozuka-pr6n/otf-up-kozuka-pr6n.map
%{_texmfdistdir}/fonts/map/dvipdfmx/jfontmaps/kozuka-pr6n/ptex-kozuka-pr6n-04.map
%{_texmfdistdir}/fonts/map/dvipdfmx/jfontmaps/kozuka-pr6n/ptex-kozuka-pr6n.map
%{_texmfdistdir}/fonts/map/dvipdfmx/jfontmaps/kozuka-pr6n/uptex-kozuka-pr6n-04.map
%{_texmfdistdir}/fonts/map/dvipdfmx/jfontmaps/kozuka-pr6n/uptex-kozuka-pr6n.map
%{_texmfdistdir}/fonts/map/dvipdfmx/jfontmaps/kozuka/otf-kozuka.map
%{_texmfdistdir}/fonts/map/dvipdfmx/jfontmaps/kozuka/otf-up-kozuka.map
%{_texmfdistdir}/fonts/map/dvipdfmx/jfontmaps/kozuka/ptex-kozuka-04.map
%{_texmfdistdir}/fonts/map/dvipdfmx/jfontmaps/kozuka/ptex-kozuka.map
%{_texmfdistdir}/fonts/map/dvipdfmx/jfontmaps/kozuka/uptex-kozuka-04.map
%{_texmfdistdir}/fonts/map/dvipdfmx/jfontmaps/kozuka/uptex-kozuka.map
%{_texmfdistdir}/fonts/map/dvipdfmx/jfontmaps/morisawa-pr6n/otf-morisawa-pr6n.map
%{_texmfdistdir}/fonts/map/dvipdfmx/jfontmaps/morisawa-pr6n/otf-up-morisawa-pr6n.map
%{_texmfdistdir}/fonts/map/dvipdfmx/jfontmaps/morisawa-pr6n/ptex-morisawa-pr6n-04.map
%{_texmfdistdir}/fonts/map/dvipdfmx/jfontmaps/morisawa-pr6n/ptex-morisawa-pr6n.map
%{_texmfdistdir}/fonts/map/dvipdfmx/jfontmaps/morisawa-pr6n/uptex-morisawa-pr6n-04.map
%{_texmfdistdir}/fonts/map/dvipdfmx/jfontmaps/morisawa-pr6n/uptex-morisawa-pr6n.map
%{_texmfdistdir}/fonts/map/dvipdfmx/jfontmaps/morisawa/otf-morisawa.map
%{_texmfdistdir}/fonts/map/dvipdfmx/jfontmaps/morisawa/otf-up-morisawa.map
%{_texmfdistdir}/fonts/map/dvipdfmx/jfontmaps/morisawa/ptex-morisawa-04.map
%{_texmfdistdir}/fonts/map/dvipdfmx/jfontmaps/morisawa/ptex-morisawa.map
%{_texmfdistdir}/fonts/map/dvipdfmx/jfontmaps/morisawa/uptex-morisawa-04.map
%{_texmfdistdir}/fonts/map/dvipdfmx/jfontmaps/morisawa/uptex-morisawa.map
%{_texmfdistdir}/fonts/map/dvipdfmx/jfontmaps/ms/otf-ms.map
%{_texmfdistdir}/fonts/map/dvipdfmx/jfontmaps/ms/otf-up-ms.map
%{_texmfdistdir}/fonts/map/dvipdfmx/jfontmaps/ms/ptex-ms.map
%{_texmfdistdir}/fonts/map/dvipdfmx/jfontmaps/ms/uptex-ms.map
%{_texmfdistdir}/fonts/map/dvipdfmx/jfontmaps/noEmbed/otf-noEmbed.map
%{_texmfdistdir}/fonts/map/dvipdfmx/jfontmaps/noEmbed/otf-up-noEmbed.map
%{_texmfdistdir}/fonts/map/dvipdfmx/jfontmaps/noEmbed/ptex-noEmbed-04.map
%{_texmfdistdir}/fonts/map/dvipdfmx/jfontmaps/noEmbed/ptex-noEmbed.map
%{_texmfdistdir}/fonts/map/dvipdfmx/jfontmaps/noEmbed/uptex-noEmbed-04.map
%{_texmfdistdir}/fonts/map/dvipdfmx/jfontmaps/noEmbed/uptex-noEmbed.map
%{_texmfdistdir}/scripts/jfontmaps/kanji-config-updmap-sys.sh
%{_texmfdistdir}/scripts/jfontmaps/kanji-config-updmap.pl
%{_texmfdistdir}/scripts/jfontmaps/kanji-fontmap-creator.pl
%doc %{_texmfdistdir}/doc/fonts/jfontmaps/ChangeLog
%doc %{_texmfdistdir}/doc/fonts/jfontmaps/ChangeLog.pre-git
%doc %{_texmfdistdir}/doc/fonts/jfontmaps/README
%doc %{_texmfdistdir}/doc/fonts/jfontmaps/examples/otf-sample-04.tex
%doc %{_texmfdistdir}/doc/fonts/jfontmaps/examples/otf-sample.tex
%doc %{_texmfdistdir}/doc/fonts/jfontmaps/examples/ptex-sample.tex
#- source
%doc %{_texmfdistdir}/source/jfontmaps/jis04cmap_exp/JISX0213-2004-H
%doc %{_texmfdistdir}/source/jfontmaps/jis04cmap_exp/JISX0213-2004-V
%doc %{_texmfdistdir}/source/jfontmaps/jis04cmap_exp/README
%doc %{_texmfdistdir}/source/jfontmaps/jis04cmap_exp/cmapdec.lua
%doc %{_texmfdistdir}/source/jfontmaps/jis04cmap_exp/jis-h04-httk.pdf
%doc %{_texmfdistdir}/source/jfontmaps/jis04cmap_exp/jis-h04-httk.tex
%doc %{_texmfdistdir}/source/jfontmaps/jis04cmap_exp/jis-v04-vttk.pdf
%doc %{_texmfdistdir}/source/jfontmaps/jis04cmap_exp/jis-v04-vttk.tex
%doc %{_texmfdistdir}/source/jfontmaps/jis04cmap_exp/jisx0213-2004-8bit-std.txt
%doc %{_texmfdistdir}/source/jfontmaps/jis04cmap_exp/mk_jis_to_aj16_cid.lua
%doc %{_texmfdistdir}/source/jfontmaps/script/updmap-otf.sh
%doc %{_texmfdistdir}/source/jfontmaps/tools/mkmap.lua
%doc %{_texmfdistdir}/source/jfontmaps/tools/release.sh

#-----------------------------------------------------------------------
%prep
%setup -c -a0 -a1 -a2

%build

%install
mkdir -p %{buildroot}%{_bindir}
pushd %{buildroot}%{_bindir}
    ln -sf %{_texmfdistdir}/scripts/jfontmaps/updmap-setup-kanji.pl updmap-setup-kanji
    ln -sf %{_texmfdistdir}/scripts/jfontmaps/updmap-setup-kanji-sys.sh updmap-setup-kanji-sys
popd
mkdir -p %{buildroot}%{_datadir}
cp -fpar texmf-dist %{buildroot}%{_datadir}
