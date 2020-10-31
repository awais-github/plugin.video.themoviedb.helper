import xbmc
import datetime
from resources.lib.helpers.plugin import PLUGINPATH, ADDONPATH, ADDON, convert_type, TYPE_PLURAL
from resources.lib.helpers.setutils import merge_two_items
from json import dumps


def _build_basedir(item_type=None, basedir=None):
    basedir = basedir or []
    items = []
    space = '' if item_type else ' '  # If only one type spaces are not needed for label because we dont add type name
    for i in basedir:
        sorting = i.pop('sorting', False)
        for i_type in i.pop('types', []):
            if item_type and item_type != i_type:
                continue
            plural = '' if item_type else convert_type(i_type, TYPE_PLURAL)  # Dont add type name to label if only one type
            item = i.copy()
            item['label'] = i.get('label', '').format(space=space, item_type=plural)
            item['params'] = i.get('params', {}).copy()
            item['params']['tmdb_type'] = i_type
            if sorting:
                item.setdefault('infoproperties', {})['tmdbhelper.context.sorting'] = dumps(item['params'])
            items.append(item)
    return items


def _get_basedir_list(item_type=None, trakt=False, tmdb=False):
    basedir = []
    if tmdb:
        basedir += _get_basedir_tmdb()
    if trakt:
        basedir += _get_basedir_trakt()
    return _build_basedir(item_type, basedir)


def _get_play_item():
    return [
        {
            'label': xbmc.getLocalizedString(208),
            'params': {'info': 'play'},
            'path': PLUGINPATH,
            'art': {'thumb': '{}/resources/poster.png'.format(ADDONPATH)},
            'types': ['movie', 'episode']}]


def _get_basedir_details():
    return [
        {
            'label': xbmc.getLocalizedString(33054),
            'params': {'info': 'seasons'},
            'path': PLUGINPATH,
            'art': {'thumb': '{}/resources/icons/tmdb/episodes.png'.format(ADDONPATH)},
            'types': ['tv']},
        {
            'label': xbmc.getLocalizedString(206),
            'params': {'info': 'cast'},
            'path': PLUGINPATH,
            'art': {'thumb': '{}/resources/icons/tmdb/cast.png'.format(ADDONPATH)},
            'types': ['movie', 'tv']},
        {
            'label': xbmc.getLocalizedString(206),
            'params': {'info': 'episode_cast'},
            'path': PLUGINPATH,
            'art': {'thumb': '{}/resources/icons/tmdb/cast.png'.format(ADDONPATH)},
            'types': ['episode']},
        {
            'label': ADDON.getLocalizedString(32223),
            'params': {'info': 'recommendations'},
            'path': PLUGINPATH,
            'art': {'thumb': '{}/resources/icons/tmdb/recommended.png'.format(ADDONPATH)},
            'types': ['movie', 'tv', 'episode']},
        {
            'label': ADDON.getLocalizedString(32224),
            'params': {'info': 'similar'},
            'path': PLUGINPATH,
            'art': {'thumb': '{}/resources/icons/tmdb/similar.png'.format(ADDONPATH)},
            'types': ['movie', 'tv', 'episode']},
        {
            'label': ADDON.getLocalizedString(32225),
            'params': {'info': 'crew'},
            'path': PLUGINPATH,
            'art': {'thumb': '{}/resources/icons/tmdb/cast.png'.format(ADDONPATH)},
            'types': ['movie', 'tv', 'episode']},
        {
            'label': ADDON.getLocalizedString(32226),
            'params': {'info': 'posters'},
            'path': PLUGINPATH,
            'art': {'thumb': '{}/resources/icons/tmdb/images.png'.format(ADDONPATH)},
            'types': ['movie', 'tv', 'episode']},
        {
            'label': xbmc.getLocalizedString(20445),
            'params': {'info': 'fanart'},
            'path': PLUGINPATH,
            'art': {'thumb': '{}/resources/icons/tmdb/images.png'.format(ADDONPATH)},
            'types': ['movie', 'tv', 'episode']},
        {
            'label': xbmc.getLocalizedString(21861),
            'params': {'info': 'movie_keywords'},
            'path': PLUGINPATH,
            'art': {'thumb': '{}/resources/icons/tmdb/tags.png'.format(ADDONPATH)},
            'types': ['movie']},
        {
            'label': ADDON.getLocalizedString(32188),
            'params': {'info': 'reviews'},
            'path': PLUGINPATH,
            'art': {'thumb': '{}/resources/icons/tmdb/reviews.png'.format(ADDONPATH)},
            'types': ['movie', 'tv', 'episode']},
        {
            'label': ADDON.getLocalizedString(32227),
            'params': {'info': 'stars_in_movies'},
            'path': PLUGINPATH,
            'art': {'thumb': '{}/resources/icons/tmdb/movies.png'.format(ADDONPATH)},
            'types': ['person']},
        {
            'label': ADDON.getLocalizedString(32228),
            'params': {'info': 'stars_in_tvshows'},
            'path': PLUGINPATH,
            'art': {'thumb': '{}/resources/icons/tmdb/tv.png'.format(ADDONPATH)},
            'types': ['person']},
        {
            'label': ADDON.getLocalizedString(32229),
            'params': {'info': 'crew_in_movies'},
            'path': PLUGINPATH,
            'art': {'thumb': '{}/resources/icons/tmdb/movies.png'.format(ADDONPATH)},
            'types': ['person']},
        {
            'label': ADDON.getLocalizedString(32230),
            'params': {'info': 'crew_in_tvshows'},
            'path': PLUGINPATH,
            'art': {'thumb': '{}/resources/icons/tmdb/tv.png'.format(ADDONPATH)},
            'types': ['person']},
        {
            'label': ADDON.getLocalizedString(32191),
            'params': {'info': 'images'},
            'path': PLUGINPATH,
            'art': {'thumb': '{}/resources/icons/tmdb/images.png'.format(ADDONPATH)},
            'types': ['person']},
        {
            'label': ADDON.getLocalizedString(32231),
            'params': {'info': 'episode_thumbs'},
            'path': PLUGINPATH,
            'art': {'thumb': '{}/resources/icons/tmdb/images.png'.format(ADDONPATH)},
            'types': ['episode']},
        {
            'label': xbmc.getLocalizedString(10025),
            'params': {'info': 'videos'},
            'path': PLUGINPATH,
            'art': {'thumb': '{}/resources/icons/tmdb/movies.png'.format(ADDONPATH)},
            'types': ['movie', 'tv', 'episode']},
        {
            'label': ADDON.getLocalizedString(32232),
            'params': {'info': 'trakt_inlists'},
            'path': PLUGINPATH,
            'art': {'thumb': '{}/resources/icons/tmdb/trakt.png'.format(ADDONPATH)},
            'types': ['null']}]


def _get_basedir_random():
    return [
        {
            'label': '{} {{item_type}}{{space}}{}'.format(
                xbmc.getLocalizedString(590), xbmc.getLocalizedString(515)),
            'types': ['movie', 'tv'],
            'params': {'info': 'random_genres'},
            'path': PLUGINPATH,
            'art': {'thumb': '{}/resources/icons/tmdb/genre.png'.format(ADDONPATH)}},
        {
            'label': '{} {{item_type}}{{space}}{}'.format(
                xbmc.getLocalizedString(590), ADDON.getLocalizedString(32117)),
            'types': ['movie'],
            'params': {'info': 'random_keyword'},
            'path': PLUGINPATH,
            'art': {'thumb': '{}/resources/poster.png'.format(ADDONPATH)}},
        {
            'label': '{}{{space}}{{item_type}}'.format(ADDON.getLocalizedString(32199)),
            'types': ['movie', 'tv'],
            'params': {'info': 'trakt_becauseyouwatched'},
            'path': PLUGINPATH,
            'art': {'thumb': '{}/resources/icons/trakt/recommended.png'.format(ADDONPATH)}},
        {
            'label': '{}{{space}}{{item_type}}'.format(ADDON.getLocalizedString(32200)),
            'types': ['movie', 'tv'],
            'params': {'info': 'trakt_becausemostwatched'},
            'path': PLUGINPATH,
            'art': {'thumb': '{}/resources/icons/trakt/recommended.png'.format(ADDONPATH)}},
        {
            'label': '{} {}{{space}}{{item_type}}'.format(
                xbmc.getLocalizedString(590), ADDON.getLocalizedString(32204)),
            'types': ['movie', 'tv'],
            'params': {'info': 'random_trending'},
            'path': PLUGINPATH,
            'art': {'thumb': '{}/resources/icons/trakt/trend.png'.format(ADDONPATH)}},
        {
            'label': '{} {}{{space}}{{item_type}}'.format(
                xbmc.getLocalizedString(590), ADDON.getLocalizedString(32175)),
            'types': ['movie', 'tv'],
            'params': {'info': 'random_popular'},
            'path': PLUGINPATH,
            'art': {'thumb': '{}/resources/icons/trakt/popular.png'.format(ADDONPATH)}},
        {
            'label': '{} {}{{space}}{{item_type}}'.format(
                xbmc.getLocalizedString(590), ADDON.getLocalizedString(32205)),
            'types': ['movie', 'tv'],
            'params': {'info': 'random_mostplayed'},
            'path': PLUGINPATH,
            'art': {'thumb': '{}/resources/icons/trakt/mostplayed.png'.format(ADDONPATH)}},
        {
            'label': '{} {}{{space}}{{item_type}}'.format(
                xbmc.getLocalizedString(590), ADDON.getLocalizedString(32206)),
            'types': ['movie', 'tv'],
            'params': {'info': 'random_anticipated'},
            'path': PLUGINPATH,
            'art': {'thumb': '{}/resources/icons/trakt/anticipated.png'.format(ADDONPATH)}},
        {
            'label': '{} {}{{space}}{{item_type}}'.format(
                xbmc.getLocalizedString(590), ADDON.getLocalizedString(32300)),
            'types': ['both'],
            'params': {'info': 'random_trendinglists'},
            'path': PLUGINPATH,
            'art': {'thumb': '{}/resources/icons/trakt/trendinglist.png'.format(ADDONPATH)}},
        {
            'label': '{} {}{{space}}{{item_type}}'.format(
                xbmc.getLocalizedString(590), ADDON.getLocalizedString(32301)),
            'types': ['both'],
            'params': {'info': 'random_popularlists'},
            'path': PLUGINPATH,
            'art': {'thumb': '{}/resources/icons/trakt/popularlist.png'.format(ADDONPATH)}},
        {
            'label': '{} {}{{space}}{{item_type}}'.format(
                xbmc.getLocalizedString(590), ADDON.getLocalizedString(32302)),
            'types': ['both'],
            'params': {'info': 'random_likedlists'},
            'path': PLUGINPATH,
            'art': {'thumb': '{}/resources/icons/trakt/likedlist.png'.format(ADDONPATH)}},
        {
            'label': '{} {}{{space}}{{item_type}}'.format(
                xbmc.getLocalizedString(590), ADDON.getLocalizedString(32303)),
            'types': ['both'],
            'params': {'info': 'random_mylists'},
            'path': PLUGINPATH,
            'art': {'thumb': '{}/resources/icons/trakt/mylists.png'.format(ADDONPATH)}}
    ]


def _get_basedir_trakt():
    return [
        {
            'label': '{{item_type}}{{space}}{}'.format(ADDON.getLocalizedString(32192)),
            'types': ['movie', 'tv'],
            'params': {'info': 'trakt_collection'},
            'path': PLUGINPATH,
            'sorting': True,
            'art': {'thumb': '{}/resources/icons/trakt/watchlist.png'.format(ADDONPATH)}},
        {
            'label': '{{item_type}}{{space}}{}'.format(ADDON.getLocalizedString(32193)),
            'types': ['movie', 'tv'],
            'params': {'info': 'trakt_watchlist'},
            'path': PLUGINPATH,
            'sorting': True,
            'art': {'thumb': '{}/resources/icons/trakt/watchlist.png'.format(ADDONPATH)}},
        {
            'label': '{}{{space}}{{item_type}}'.format(ADDON.getLocalizedString(32194)),
            'types': ['movie', 'tv'],
            'params': {'info': 'trakt_history'},
            'path': PLUGINPATH,
            'art': {'thumb': '{}/resources/icons/trakt/recentlywatched.png'.format(ADDONPATH)}},
        {
            'label': '{}{{space}}{{item_type}}'.format(ADDON.getLocalizedString(32195)),
            'types': ['movie', 'tv'],
            'params': {'info': 'trakt_mostwatched'},
            'path': PLUGINPATH,
            'art': {'thumb': '{}/resources/icons/trakt/mostwatched.png'.format(ADDONPATH)}},
        {
            'label': '{}{{space}}{{item_type}}'.format(ADDON.getLocalizedString(32196)),
            'types': ['movie', 'tv'],
            'params': {'info': 'trakt_inprogress'},
            'path': PLUGINPATH,
            'sorting': True,
            'art': {'thumb': '{}/resources/icons/trakt/inprogress.png'.format(ADDONPATH)}},
        {
            'label': ADDON.getLocalizedString(32197),
            'types': ['tv'],
            'params': {'info': 'trakt_nextepisodes'},
            'path': PLUGINPATH,
            'art': {'thumb': '{}/resources/icons/trakt/inprogress.png'.format(ADDONPATH)}},
        {
            'label': '{{item_type}}{{space}}{}'.format(ADDON.getLocalizedString(32198)),
            'types': ['movie', 'tv'],
            'params': {'info': 'trakt_recommendations'},
            'path': PLUGINPATH,
            'art': {'thumb': '{}/resources/icons/trakt/recommended.png'.format(ADDONPATH)}},
        {
            'label': '{}{{space}}{{item_type}}'.format(ADDON.getLocalizedString(32199)),
            'types': ['movie', 'tv'],
            'params': {'info': 'trakt_becauseyouwatched'},
            'path': PLUGINPATH,
            'art': {'thumb': '{}/resources/icons/trakt/recommended.png'.format(ADDONPATH)}},
        {
            'label': '{}{{space}}{{item_type}}'.format(ADDON.getLocalizedString(32200)),
            'types': ['movie', 'tv'],
            'params': {'info': 'trakt_becausemostwatched'},
            'path': PLUGINPATH,
            'art': {'thumb': '{}/resources/icons/trakt/recommended.png'.format(ADDONPATH)}},
        {
            'label': '{} {{item_type}}{{space}}{}'.format(ADDON.getLocalizedString(32201), ADDON.getLocalizedString(32202)),
            'types': ['tv'],
            'params': {'info': 'trakt_myairing'},
            'path': PLUGINPATH,
            'art': {'thumb': '{}/resources/icons/trakt/airing.png'.format(ADDONPATH)}},
        {
            'label': '{} {{item_type}}{{space}}{}'.format(ADDON.getLocalizedString(32201), ADDON.getLocalizedString(32203)),
            'types': ['tv'],
            'params': {'info': 'dir_calendar_trakt'},
            'path': PLUGINPATH,
            'art': {'thumb': '{}/resources/icons/trakt/calendar.png'.format(ADDONPATH)}},
        {
            'label': '{}{{space}}{{item_type}}'.format(ADDON.getLocalizedString(32204)),
            'types': ['movie', 'tv'],
            'params': {'info': 'trakt_trending'},
            'path': PLUGINPATH,
            'art': {'thumb': '{}/resources/icons/trakt/trend.png'.format(ADDONPATH)}},
        {
            'label': '{}{{space}}{{item_type}}'.format(ADDON.getLocalizedString(32175)),
            'types': ['movie', 'tv'],
            'params': {'info': 'trakt_popular'},
            'path': PLUGINPATH,
            'art': {'thumb': '{}/resources/icons/trakt/popular.png'.format(ADDONPATH)}},
        {
            'label': '{}{{space}}{{item_type}}'.format(ADDON.getLocalizedString(32205)),
            'types': ['movie', 'tv'],
            'params': {'info': 'trakt_mostplayed'},
            'path': PLUGINPATH,
            'art': {'thumb': '{}/resources/icons/trakt/mostplayed.png'.format(ADDONPATH)}},
        {
            'label': '{}{{space}}{{item_type}}'.format(ADDON.getLocalizedString(32206)),
            'types': ['movie', 'tv'],
            'params': {'info': 'trakt_anticipated'},
            'path': PLUGINPATH,
            'art': {'thumb': '{}/resources/icons/trakt/anticipated.png'.format(ADDONPATH)}},
        {
            'label': '{}{{space}}{{item_type}}'.format(ADDON.getLocalizedString(32207)),
            'types': ['movie'],
            'params': {'info': 'trakt_boxoffice'},
            'path': PLUGINPATH,
            'art': {'thumb': '{}/resources/icons/trakt/boxoffice.png'.format(ADDONPATH)}},
        {
            'label': ADDON.getLocalizedString(32208),
            'types': ['both'],
            'params': {'info': 'trakt_trendinglists'},
            'path': PLUGINPATH,
            'art': {'thumb': '{}/resources/icons/trakt/trendinglist.png'.format(ADDONPATH)}},
        {
            'label': ADDON.getLocalizedString(32209),
            'types': ['both'],
            'params': {'info': 'trakt_popularlists'},
            'path': PLUGINPATH,
            'art': {'thumb': '{}/resources/icons/trakt/popularlist.png'.format(ADDONPATH)}},
        {
            'label': ADDON.getLocalizedString(32210),
            'types': ['both'],
            'params': {'info': 'trakt_likedlists'},
            'path': PLUGINPATH,
            'art': {'thumb': '{}/resources/icons/trakt/likedlist.png'.format(ADDONPATH)}},
        {
            'label': ADDON.getLocalizedString(32211),
            'types': ['both'],
            'params': {'info': 'trakt_mylists'},
            'path': PLUGINPATH,
            'art': {'thumb': '{}/resources/icons/trakt/mylists.png'.format(ADDONPATH)}}]


def _get_basedir_tmdb():
    return [
        {
            'label': '{}{{space}}{{item_type}}'.format(xbmc.getLocalizedString(137)),
            'types': ['movie', 'tv', 'person'],
            'params': {'info': 'dir_search'},
            'path': PLUGINPATH,
            'art': {'thumb': '{}/resources/icons/tmdb/search.png'.format(ADDONPATH)}},
        {
            'label': '{}{{space}}{{item_type}}'.format(ADDON.getLocalizedString(32175)),
            'types': ['movie', 'tv', 'person'],
            'params': {'info': 'popular'},
            'path': PLUGINPATH,
            'art': {'thumb': '{}/resources/icons/tmdb/popular.png'.format(ADDONPATH)}},
        {
            'label': '{}{{space}}{{item_type}}'.format(ADDON.getLocalizedString(32176)),
            'types': ['movie', 'tv'],
            'params': {'info': 'top_rated'},
            'path': PLUGINPATH,
            'art': {'thumb': '{}/resources/icons/tmdb/toprated.png'.format(ADDONPATH)}},
        {
            'label': '{}{{space}}{{item_type}}'.format(ADDON.getLocalizedString(32177)),
            'types': ['movie'],
            'params': {'info': 'upcoming'},
            'path': PLUGINPATH,
            'art': {'thumb': '{}/resources/icons/tmdb/upcoming.png'.format(ADDONPATH)}},
        {
            'label': '{{item_type}}{{space}}{}'.format(ADDON.getLocalizedString(32178)),
            'types': ['movie', 'tv', 'person'],
            'params': {'info': 'trending_day'},
            'path': PLUGINPATH,
            'art': {'thumb': '{}/resources/icons/tmdb/upcoming.png'.format(ADDONPATH)}},
        {
            'label': '{{item_type}}{{space}}{}'.format(ADDON.getLocalizedString(32179)),
            'types': ['movie', 'tv', 'person'],
            'params': {'info': 'trending_week'},
            'path': PLUGINPATH,
            'art': {'thumb': '{}/resources/icons/tmdb/upcoming.png'.format(ADDONPATH)}},
        {
            'label': ADDON.getLocalizedString(32180),
            'types': ['movie'],
            'params': {'info': 'now_playing'},
            'path': PLUGINPATH,
            'art': {'thumb': '{}/resources/icons/tmdb/intheatres.png'.format(ADDONPATH)}},
        {
            'label': ADDON.getLocalizedString(32181),
            'types': ['tv'],
            'params': {'info': 'airing_today'},
            'path': PLUGINPATH,
            'art': {'thumb': '{}/resources/icons/tmdb/airing.png'.format(ADDONPATH)}},
        {
            'label': ADDON.getLocalizedString(32182),
            'types': ['tv'],
            'params': {'info': 'on_the_air'},
            'path': PLUGINPATH,
            'art': {'thumb': '{}/resources/icons/tmdb/airing.png'.format(ADDONPATH)}},
        {
            'label': ADDON.getLocalizedString(32183),
            'types': ['tv'],
            'params': {'info': 'dir_calendar_library'},
            'path': PLUGINPATH,
            'art': {'thumb': '{}/resources/icons/tmdb/airing.png'.format(ADDONPATH)}},
        {
            'label': '{{item_type}}{{space}}{}'.format(xbmc.getLocalizedString(135)),
            'types': ['movie', 'tv'],
            'params': {'info': 'genres'},
            'path': PLUGINPATH,
            'art': {'thumb': '{}/resources/icons/tmdb/genre.png'.format(ADDONPATH)}},
        {
            'label': '{}{{space}}{{item_type}}'.format(ADDON.getLocalizedString(32184)),
            'types': ['movie'],
            'params': {'info': 'revenue_movies'},
            'path': PLUGINPATH,
            'art': {'thumb': '{}/resources/poster.png'.format(ADDONPATH)}},
        {
            'label': '{}{{space}}{{item_type}}'.format(ADDON.getLocalizedString(32185)),
            'types': ['movie', 'tv'],
            'params': {'info': 'most_voted'},
            'path': PLUGINPATH,
            'art': {'thumb': '{}/resources/poster.png'.format(ADDONPATH)}},
        {
            'label': '{}{{space}}{{item_type}}'.format(ADDON.getLocalizedString(32186)),
            'types': ['collection', 'keyword', 'network', 'studio'],
            'params': {'info': 'all_items'},
            'path': PLUGINPATH,
            'art': {'thumb': '{}/resources/poster.png'.format(ADDONPATH)}}]


def _get_basedir_main():
    return [
        {
            'label': xbmc.getLocalizedString(342),
            'params': {'info': 'dir_movie'},
            'path': PLUGINPATH,
            'art': {'thumb': '{}/resources/icons/tmdb/movies.png'.format(ADDONPATH)}},
        {
            'label': xbmc.getLocalizedString(20343),
            'params': {'info': 'dir_tv'},
            'path': PLUGINPATH,
            'art': {'thumb': '{}/resources/icons/tmdb/tv.png'.format(ADDONPATH)}},
        {
            'label': ADDON.getLocalizedString(32172),
            'params': {'info': 'dir_person'},
            'path': PLUGINPATH,
            'art': {'thumb': '{}/resources/icons/tmdb/cast.png'.format(ADDONPATH)}},
        {
            'label': ADDON.getLocalizedString(32173),
            'params': {'info': 'dir_random'},
            'path': PLUGINPATH,
            'art': {'thumb': '{}/resources/poster.png'.format(ADDONPATH)}},
        {
            'label': ADDON.getLocalizedString(32174),
            'params': {'info': 'dir_discover'},
            'path': PLUGINPATH,
            'art': {'thumb': '{}/resources/poster.png'.format(ADDONPATH)}},
        {
            'label': 'TheMovieDb',
            'params': {'info': 'dir_tmdb'},
            'path': PLUGINPATH,
            'art': {'thumb': '{}/resources/poster.png'.format(ADDONPATH)}},
        {
            'label': 'Trakt',
            'params': {'info': 'dir_trakt'},
            'path': PLUGINPATH,
            'art': {'thumb': '{}/resources/trakt.png'.format(ADDONPATH)}}]


def _get_basedir_calendar_items():
    return [
        {
            'label': ADDON.getLocalizedString(32280),
            'params': {'startdate': -14, 'days': 14},
            'path': PLUGINPATH,
            'info_types': ['trakt_calendar', 'library_nextaired'],
            'art': {'thumb': '{}/resources/poster.png'.format(ADDONPATH)}},
        {
            'label': ADDON.getLocalizedString(32281),
            'params': {'startdate': -7, 'days': 7},
            'path': PLUGINPATH,
            'info_types': ['trakt_calendar', 'library_nextaired'],
            'art': {'thumb': '{}/resources/poster.png'.format(ADDONPATH)}},
        {
            'label': ADDON.getLocalizedString(32282),
            'params': {'startdate': -1, 'days': 1},
            'path': PLUGINPATH,
            'info_types': ['trakt_calendar', 'library_nextaired'],
            'art': {'thumb': '{}/resources/poster.png'.format(ADDONPATH)}},
        {
            'label': xbmc.getLocalizedString(33006),
            'params': {'startdate': 0, 'days': 1},
            'path': PLUGINPATH,
            'info_types': ['trakt_calendar', 'library_nextaired'],
            'art': {'thumb': '{}/resources/poster.png'.format(ADDONPATH)}},
        {
            'label': xbmc.getLocalizedString(33007),
            'params': {'startdate': 1, 'days': 1},
            'path': PLUGINPATH,
            'info_types': ['trakt_calendar', 'library_nextaired'],
            'art': {'thumb': '{}/resources/poster.png'.format(ADDONPATH)}},
        {
            'label': '{weekday}',
            'params': {'startdate': 2, 'days': 1},
            'path': PLUGINPATH,
            'info_types': ['trakt_calendar', 'library_nextaired'],
            'art': {'thumb': '{}/resources/poster.png'.format(ADDONPATH)}},
        {
            'label': '{weekday}',
            'params': {'startdate': 3, 'days': 1},
            'path': PLUGINPATH,
            'info_types': ['trakt_calendar', 'library_nextaired'],
            'art': {'thumb': '{}/resources/poster.png'.format(ADDONPATH)}},
        {
            'label': '{weekday}',
            'params': {'startdate': 4, 'days': 1},
            'path': PLUGINPATH,
            'info_types': ['trakt_calendar', 'library_nextaired'],
            'art': {'thumb': '{}/resources/poster.png'.format(ADDONPATH)}},
        {
            'label': '{weekday}',
            'params': {'startdate': 5, 'days': 1},
            'path': PLUGINPATH,
            'info_types': ['trakt_calendar', 'library_nextaired'],
            'art': {'thumb': '{}/resources/poster.png'.format(ADDONPATH)}},
        {
            'label': '{weekday}',
            'params': {'startdate': 6, 'days': 1},
            'path': PLUGINPATH,
            'info_types': ['trakt_calendar', 'library_nextaired'],
            'art': {'thumb': '{}/resources/poster.png'.format(ADDONPATH)}},
        {
            'label': ADDON.getLocalizedString(32284),
            'params': {'startdate': 0, 'days': 7},
            'path': PLUGINPATH,
            'info_types': ['trakt_calendar', 'library_nextaired'],
            'art': {'thumb': '{}/resources/poster.png'.format(ADDONPATH)}},
        {
            'label': ADDON.getLocalizedString(32285),
            'params': {'startdate': 0, 'days': 14},
            'path': PLUGINPATH,
            'info_types': ['trakt_calendar', 'library_nextaired'],
            'art': {'thumb': '{}/resources/poster.png'.format(ADDONPATH)}}]


def _get_basedir_calendar(info=None):
    items = []
    today = datetime.datetime.today()
    for i in _get_basedir_calendar_items():
        if info not in i['info_types']:
            continue
        date = today + datetime.timedelta(days=i.get('params', {}).get('startdate', 0))
        i['label'] = i['label'].format(weekday=date.strftime('%A'))
        i['params']['info'] = info
        items.append(i)
    return items


def get_basedir_details(tmdb_type, tmdb_id, season=None, episode=None, detailed_item=None, include_play=False):
    base_item = detailed_item or {}
    base_item.setdefault('params', {})
    base_item.setdefault('infolabels', {})
    base_item['path'] = PLUGINPATH
    base_item['params']['tmdb_id'] = tmdb_id
    base_item['params']['tmdb_type'] = tmdb_type
    base_item['params']['info'] = 'details'

    basedir_items = []
    if tmdb_type == 'movie':
        base_item['infolabels']['mediatype'] = 'movie'
        basedir_items = _build_basedir('movie', _get_play_item()) if include_play else []
        basedir_items += _build_basedir('movie', _get_basedir_details())
    elif tmdb_type == 'tv' and season is not None and episode is not None:
        base_item['params']['season'] = season
        base_item['params']['episode'] = episode
        base_item['infolabels']['mediatype'] = 'episode'
        basedir_items = _build_basedir('episode', _get_play_item()) if include_play else []
        basedir_items += _build_basedir('tv', _get_basedir_details())
    elif tmdb_type == 'tv' and season is not None:
        base_item['params']['info'] = 'episodes'
        base_item['params']['season'] = season
        base_item['infolabels']['mediatype'] = 'season'
        basedir_items = _build_basedir('season', _get_basedir_details())
    elif tmdb_type == 'tv':
        base_item['params']['info'] = 'seasons'
        base_item['infolabels']['mediatype'] = 'tvshow'
        basedir_items = _build_basedir('tv', _get_basedir_details())
    elif tmdb_type == 'person':
        base_item['infolabels']['mediatype'] = 'video'
        basedir_items = _build_basedir('person', _get_basedir_details())

    items = [merge_two_items(base_item, i) for i in basedir_items if i]

    if detailed_item:
        return [base_item] + items
    return items


class BaseDirLists():
    def list_basedir(self, info=None):
        if not info:
            return _get_basedir_main()
        if info == 'dir_movie':
            return _get_basedir_list('movie', tmdb=True, trakt=True)
        if info == 'dir_tv':
            return _get_basedir_list('tv', tmdb=True, trakt=True)
        if info == 'dir_person':
            return _get_basedir_list('person', tmdb=True, trakt=True)
        if info == 'dir_tmdb':
            return _get_basedir_list(None, tmdb=True)
        if info == 'dir_trakt':
            return _get_basedir_list(None, trakt=True)
        if info == 'dir_random':
            return _build_basedir(None, _get_basedir_random())
        if info == 'dir_calendar_trakt':
            return _get_basedir_calendar(info='trakt_calendar')
        if info == 'dir_calendar_library':
            return _get_basedir_calendar(info='library_nextaired')

    def list_details(self, tmdb_type, tmdb_id, season=None, episode=None, **kwargs):
        base_item = self.tmdb_api.get_details(tmdb_type, tmdb_id, season, episode)
        items = get_basedir_details(tmdb_type, tmdb_id, season, episode, base_item)
        self.container_content = self.get_container_content(tmdb_type, season, episode)
        return items