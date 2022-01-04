import React from "react";
import styled from "styled-components";

const GarmentItemContainer = styled.div`
  width: 100%;
  min-height: 6em;
  display: flex;
  border-bottom: 2px solid #d8d8d852;
  padding: 6px 8px;
  align-items: center;
`;

const Thumbnail = styled.div`
  width: auto;
  height: 100%;
  display: flex;
  flex: 0.4;

  img {
    width: auto;
    height: 100%;
  }
`;

const ProductTitle = styled.h3`
  font-size: 15px;
  color: #000;
  margin-left: 10px;
  flex: 2;
  display: flex;
`;

const Stock = styled.span`
  font-size: 10px;
  color: #a1a1a1;
  margin-left: 25px;
  flex: 1;
  display: flex;
`;

const Price = styled.span`
  color: #a1a1a1;
  font-size: 16px;
  display: flex;
  flex: 0.2;
`;

const Currency = styled.span`
  color: #a1a1a1;
  font-size: 10px;
  display: flex;
  flex: 0.2;
  margin-left: 3px;
`;

export function GarmentItem(props) {
  const { thumbanilSrc, name, stock, price, currency } = props;

  return (
    <GarmentItemContainer>
      <Thumbnail>
        <img src={thumbanilSrc} />
      </Thumbnail>
      <ProductTitle>{name}</ProductTitle>
      <Stock>Stock: {stock}</Stock>
      <Price>{price}</Price>
      <Currency>{currency}</Currency>
    </GarmentItemContainer>
  );
}
