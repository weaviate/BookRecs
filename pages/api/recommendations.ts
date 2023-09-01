// Next.js API route support: https://nextjs.org/docs/api-routes/introduction
import { NearTextType } from 'types';
import type { NextApiRequest, NextApiResponse } from 'next';
import weaviate, { WeaviateClient, ApiKey } from 'weaviate-ts-client';


export default async function handler(
  req: NextApiRequest,
  res: NextApiResponse<Object>
) {
  try {
    const { method } = req;
    let { query } = req.body;

    switch (method) {

      case 'POST': {
        const client: WeaviateClient = weaviate.client({
          scheme: 'https',
          host: process.env.WEAVIATE_CLUSTER_URL || 'zxzyqcyksbw7ozpm5yowa.c0.us-west2.gcp.weaviate.cloud',
          apiKey: new ApiKey(process.env.WEAVIATE_API_KEY || 'n6mdfI32xrXF3DH76i8Pwc2IajzLZop2igb6'), //READONLY API Key, ensure the environment variable is an Admin key to support writing
          headers: {
            'X-OpenAI-Api-Key': process.env.OPENAI_APIKEY!,
          },
        });

        let nearText: NearTextType = {
          concepts: [],
        }

        nearText.certainty = .6

        nearText.concepts = query;

        const recData = await client.graphql
          .get()
          .withClassName('Book')
          .withFields(
            'title isbn10 isbn13  categories thumbnail description num_pages average_rating published_year authors'
          )
          .withNearText(nearText)
          .withLimit(20)
          .do();

        res.status(200).json(recData);
        break;
      }
      default:
        res.status(400);
        break;
    }
  } catch (err) {
    console.error(err);
    res.status(500);
  }
}
