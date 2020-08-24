import discord


default_embed_color = 0xffffff


async def beatmapset_array(mapset, color=default_embed_color):
    if mapset:
        body = f""

        sorted_diffs = sorted(mapset["beatmaps"], key=lambda k: k["difficulty_rating"])
        for beatmap in sorted_diffs:
            try:
                short_dec = str(beatmap["difficulty_rating"])
                body += f"{short_dec} ☆ {beatmap['version']} [{beatmap['mode']}] \n"
            except:
                pass
        if len(body) > 2048:
            body = ""
        embed = discord.Embed(
            title=f"{mapset['artist']} - {mapset['title']}",
            url=f"https://osu.ppy.sh/beatmapsets/{mapset['id']}",
            description=body,
            color=int(color)
        )
        embed.set_author(
            name=mapset['creator'],
            url=f"https://osu.ppy.sh/users/{mapset['user_id']}",
            icon_url=f"https://a.ppy.sh/{mapset['user_id']}",
        )
        embed.set_thumbnail(
            url=f"https://assets.ppy.sh/beatmaps/{mapset['id']}/covers/list@2x.jpg"
        )
        embed.set_footer(
            text=mapset["source"],
        )
        return embed
    else:
        return None


async def user_array(user, color=default_embed_color, custom_footer=""):
    if user:
        body = ""

        if user["country"]:
            try:
                country = user["country"]
                country_flag_emote = f":flag_{country['code'].lower()}:"
                body += f"{country_flag_emote} {country['name']}\n"
            except:
                pass

        if user.pp:
            body += f"{user['statistics']['pp']}pp (#{user['statistics']['pp_rank']})\n"

        body += f"Joined osu on: {user['join_date']}\n"

        embed = discord.Embed(
            title=user["username"],
            url=f"https://osu.ppy.sh/users/{user['id']}",
            color=color,
            description=body,
        )
        embed.set_thumbnail(
            url=user["avatar_url"]
        )
        embed.set_footer(
            text=custom_footer
        )
        return embed
    else:
        return None
