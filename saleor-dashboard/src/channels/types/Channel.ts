/* tslint:disable */
/* eslint-disable */
// @generated
// This file was automatically generated and should not be edited.

// ====================================================
// GraphQL query operation: Channel
// ====================================================

export interface Channel_channel_defaultCountry {
  __typename: "CountryDisplay";
  code: string;
  country: string;
}

export interface Channel_channel {
  __typename: "Channel";
  id: string;
  isActive: boolean;
  name: string;
  slug: string;
  currencyCode: string;
  defaultCountry: Channel_channel_defaultCountry;
  hasOrders: boolean;
}

export interface Channel {
  channel: Channel_channel | null;
}

export interface ChannelVariables {
  id: string;
}
