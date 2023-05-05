SELECT
    *
FROM facebook_posts
WHERE
    post_id IN (
				SELECT post_id 
				FROM facebook_reactions
				WHERE reaction = 'heart');